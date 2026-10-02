from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, email, user_id):
        if not self.is_valid_email(email):
            raise ValueError("A valid email address is required.")
        self._name = name
        self._email = email
        self._user_id = user_id

    @staticmethod
    def is_valid_email(email):
        """Return whether an address has a basic valid email format."""
        if not isinstance(email, str) or "@" not in email:
            return False
        local_part, domain = email.rsplit("@", 1)
        return bool(local_part and "." in domain and not domain.startswith("."))

    @classmethod
    def from_data(cls, data):
        """Create the concrete user type from a mapping of user fields."""
        return cls(data["name"], data["email"], data["user_id"])

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def user_id(self):
        return self._user_id

    @abstractmethod
    def show_profile(self):
        """Display profile information for the concrete user type."""
        raise NotImplementedError


class Student(User):
    """Child class representing a student."""

    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self._enrolled_courses = []

    @property
    def enrolled_courses(self):
        return tuple(self._enrolled_courses)

    def enroll_course(self, course):
        """Enroll the student in a course."""
        self._enrolled_courses.append(course)
        print(f"{self.name} enrolled in {course}.")

    def show_courses(self):
        """Display the student's enrolled courses."""
        print(f"{self.name}'s enrolled courses:")

        if self._enrolled_courses:
            for course in self._enrolled_courses:
                print(f"- {course}")
        else:
            print("No courses enrolled.")

    def show_profile(self):
        """Override the parent show_profile method."""
        print("\n--- Student Profile ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Student ID: {self.user_id}")
        print(f"Courses enrolled: {len(self._enrolled_courses)}")


class Mentor(User):
    """Child class representing a mentor."""

    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self._created_courses = []

    @property
    def created_courses(self):
        return tuple(self._created_courses)

    def create_course(self, course):
        """Create a new course."""
        self._created_courses.append(course)
        print(f"{self.name} created the course: {course}")

    def show_courses(self):
        """Display courses created by the mentor."""
        print(f"{self.name}'s courses:")

        if self._created_courses:
            for course in self._created_courses:
                print(f"- {course}")
        else:
            print("No courses created.")

    def show_profile(self):
        """Override the parent show_profile method."""
        print("\n--- Mentor Profile ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Mentor ID: {self.user_id}")
        print(f"Courses created: {len(self._created_courses)}")


class Admin(User):
    """Child class representing an administrator."""

    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self._users = []

    @property
    def users(self):
        return tuple(self._users)

    def add_user(self, user):
        """Add a user to the platform."""
        self._users.append(user)
        print(f"{user.name} was added to the platform.")

    def show_users(self):
        """Display all users managed by the admin."""
        print("\nUsers on the platform:")

        for user in self._users:
            print(f"- {user.name} ({user.__class__.__name__})")

    def show_profile(self):
        """Override the parent show_profile method."""
        print("\n--- Admin Profile ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Admin ID: {self.user_id}")
        print(f"Users managed: {len(self._users)}")


def main():
    # Create objects
    student = Student.from_data({
        "name": "Alice",
        "email": "alice@example.com",
        "user_id": "S001",
    })

    mentor = Mentor(
        "John",
        "john@example.com",
        "M001"
    )

    admin = Admin(
        "Sarah",
        "sarah@example.com",
        "A001"
    )

    # Student functionality
    print("=== STUDENT ===")
    student.enroll_course("Python Basics")
    student.enroll_course("Object-Oriented Programming")
    student.show_courses()

    # Mentor functionality
    print("\n=== MENTOR ===")
    mentor.create_course("Python Basics")
    mentor.create_course("Object-Oriented Programming")
    mentor.show_courses()

    # Admin functionality
    print("\n=== ADMIN ===")
    admin.add_user(student)
    admin.add_user(mentor)
    admin.show_users()

    # Demonstrate method overriding
    print("\n=== METHOD OVERRIDING ===")

    student.show_profile()
    mentor.show_profile()
    admin.show_profile()


if __name__ == "__main__":
    main()
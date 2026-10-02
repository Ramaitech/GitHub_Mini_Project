from abc import ABC, abstractmethod


class Course:
    """A course offered on the learning platform."""

    def __init__(self, course_id, title):
        if not isinstance(course_id, str) or not course_id.strip():
            raise ValueError("A course ID is required.")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("A course title is required.")
        self._course_id = course_id.strip()
        self._title = title.strip()

    @property
    def course_id(self):
        return self._course_id

    @property
    def title(self):
        return self._title


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
        self._enrollments = []

    @property
    def enrolled_courses(self):
        return tuple(enrollment.course for enrollment in self._enrollments)

    @property
    def enrollments(self):
        return tuple(self._enrollments)

    def enroll_course(self, course):
        """Enroll the student in a course."""
        if not isinstance(course, Course):
            raise TypeError("course must be a Course instance.")
        enrollment = Enrollment(self, course)
        self._enrollments.append(enrollment)
        print(f"{self.name} enrolled in {course.title}.")
        return enrollment

    def show_courses(self):
        """Display the student's enrolled courses."""
        print(f"{self.name}'s enrolled courses:")

        if self._enrollments:
            for enrollment in self._enrollments:
                print(f"- {enrollment.course.title}")
        else:
            print("No courses enrolled.")

    def show_profile(self):
        """Override the parent show_profile method."""
        print("\n--- Student Profile ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Student ID: {self.user_id}")
        print(f"Courses enrolled: {len(self._enrollments)}")


class Enrollment:
    """The association between a student and a course."""

    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise TypeError("student must be a Student instance.")
        if not isinstance(course, Course):
            raise TypeError("course must be a Course instance.")
        self._student = student
        self._course = course

    @property
    def student(self):
        return self._student

    @property
    def course(self):
        return self._course


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
        if not isinstance(course, Course):
            raise TypeError("course must be a Course instance.")
        self._created_courses.append(course)
        print(f"{self.name} created the course: {course.title}")

    def show_courses(self):
        """Display courses created by the mentor."""
        print(f"{self.name}'s courses:")

        if self._created_courses:
            for course in self._created_courses:
                print(f"- {course.title}")
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
    python_course = Course("C001", "Python Basics")
    oop_course = Course("C002", "Object-Oriented Programming")

    # Student functionality
    print("=== STUDENT ===")
    student.enroll_course(python_course)
    student.enroll_course(oop_course)
    student.show_courses()

    # Mentor functionality
    print("\n=== MENTOR ===")
    mentor.create_course(python_course)
    mentor.create_course(oop_course)
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
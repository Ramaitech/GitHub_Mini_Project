    
class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def show_profile(self):
        """Display basic user information."""
        print(f"User: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")


class Student(User):
    """Child class representing a student."""

    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.enrolled_courses = []

    def enroll_course(self, course):
        """Enroll the student in a course."""
        self.enrolled_courses.append(course)
        print(f"{self.name} enrolled in {course}.")

    def show_courses(self):
        """Display the student's enrolled courses."""
        print(f"{self.name}'s enrolled courses:")

        if self.enrolled_courses:
            for course in self.enrolled_courses:
                print(f"- {course}")
        else:
            print("No courses enrolled.")

    def show_profile(self):
        """Override the parent show_profile method."""
        print("\n--- Student Profile ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Student ID: {self.user_id}")
        print(f"Courses enrolled: {len(self.enrolled_courses)}")


class Mentor(User):
    """Child class representing a mentor."""

    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.created_courses = []

    def create_course(self, course):
        """Create a new course."""
        self.created_courses.append(course)
        print(f"{self.name} created the course: {course}")

    def show_courses(self):
        """Display courses created by the mentor."""
        print(f"{self.name}'s courses:")

        if self.created_courses:
            for course in self.created_courses:
                print(f"- {course}")
        else:
            print("No courses created.")

    def show_profile(self):
        """Override the parent show_profile method."""
        print("\n--- Mentor Profile ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Mentor ID: {self.user_id}")
        print(f"Courses created: {len(self.created_courses)}")


class Admin(User):
    """Child class representing an administrator."""

    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.users = []

    def add_user(self, user):
        """Add a user to the platform."""
        self.users.append(user)
        print(f"{user.name} was added to the platform.")

    def show_users(self):
        """Display all users managed by the admin."""
        print("\nUsers on the platform:")

        for user in self.users:
            print(f"- {user.name} ({user.__class__.__name__})")

    def show_profile(self):
        """Override the parent show_profile method."""
        print("\n--- Admin Profile ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Admin ID: {self.user_id}")
        print(f"Users managed: {len(self.users)}")


def main():
    # Create objects
    student = Student(
        "Alice",
        "alice@example.com",
        "S001"
    )

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
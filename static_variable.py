class Student:
    # Class variable
    college_name = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, College: {Student.college_name}")

    # Classmethod
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    # Staticmethod
    @staticmethod
    def is_pass(marks):
        return "Pass" if marks >= 35 else "Fail"


# Test
s1 = Student("Alice", 101)
s2 = Student("Bob", 102)

s1.display()
s2.display()

# Change college name
Student.change_college("XYZ College")

s1.display()
s2.display()

# Check pass/fail
print(Student.is_pass(40))  # Pass
print(Student.is_pass(30))  # Fail

class Person:
    def __init__(self, name, **kwargs):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, student_id, **kwargs):
        super().__init__(name, **kwargs)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")


class SportsPlayer(Person):
    def __init__(self, name, sport_name, **kwargs):
        super().__init__(name, **kwargs)
        self.sport_name = sport_name

    def display(self):
        super().display()
        print(f"Sport: {self.sport_name}")


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name, **kwargs):
        super().__init__(name=name, student_id=student_id, sport_name=sport_name, **kwargs)
        self.college_name = college_name

    def display(self):
        super().display()
        print(f"College: {self.college_name}")

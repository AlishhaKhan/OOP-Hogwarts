# teacher class

# Inheritance + Polymorphism + Class Method

from classes.student import Student

class Teacher:
    total_teachers = 0  # Static Variable

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        Teacher.total_teachers += 1

    @classmethod
    def get_teacher_count(cls):  # Class Method
        return cls.total_teachers

    def display_info(self):  # Polymorphism
        return f"Prof. {self.name} teaches {self.subject}"

    def __str__(self):
        return f"Prof. {self.name}"

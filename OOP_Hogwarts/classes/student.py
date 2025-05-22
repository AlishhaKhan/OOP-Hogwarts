# student class with oop

#  Base Class for Students (Encapsulation, Constructor, Dunder Methods)

class Student:
    school_name = "OOP Hogwarts"  # Static Variable (shared across all)

    def __init__(self, name, house, marks=0):
        self.name = name
        self.house = house
        self.__marks = marks  # Encapsulated variable

    def __str__(self):
        return f"{self.name} from {self.house} House"

    @property
    def marks(self):  # Getter
        return self.__marks

    @marks.setter
    def marks(self, value):  # Setter
        if 0 <= value <= 100:
            self.__marks = value

    def display_info(self):
        return f"Name: {self.name}, House: {self.house}, Marks: {self.__marks}"

    def __del__(self):
        print(f"Student {self.name} removed from database.")

# classroom system (composition/aggregation) 

class Classroom:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher  # Aggregation (not owned, just linked)
        self.students = []      # Composition (owned)

    def add_student(self, student):
        self.students.append(student)

    def __len__(self):  # Dunder Method
        return len(self.students)

    def __getitem__(self, index):  # Dunder Method
        return self.students[index]

    def display_info(self):
        return {
            "Class": self.name,
            "Teacher": str(self.teacher),
            "Students": [str(s) for s in self.students]
        }

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"{self.name} draws the beautiful drawing")


class drawing:
    def __init__(self, draws):
        self.draws = draws

    def show(self):
        print(f"{self.draws} is made by the students")


class StudentDrawing(drawing, Student):
    def __init__(self, name, draws):
        self.name = name
        self.draws = draws


sd = StudentDrawing("Riya", "sunsetscenario")
sd.show()

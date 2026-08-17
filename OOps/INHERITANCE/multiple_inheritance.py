class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"{self.name} perform dance")


class dance:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


# class DanceEmployee(Employee,dance):  Doing this will run the Employee class method
class DanceEmployee(dance, Employee):  # doing this runs the method of dance class
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance


de = DanceEmployee("Riya", "Kathak")
de.show()

# Example of multilevel inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def work(self):
        print(f"{self.name}  having id {self.employee_id} is working")


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def group(self):
        print(f"{self.name} works with {self.team_size} members")


M = Manager("Riya", 2, 15)
M.introduce()
M.work()
M.group()

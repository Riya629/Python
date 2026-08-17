class Employee:
    def display_employee(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"Name: {self.name}\n Salary:{self.salary}")
class Manager(Employee):
    def display_manager(self,department):
        self.department=department
        print(f"Department:{self.department}")

M=Manager()
M.display_employee("Riya",20000)
M.display_manager("BCA")


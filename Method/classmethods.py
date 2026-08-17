class Employee:
    company="Apple"
    def show(self):
        print(f'The name is {self.name} and company is {self.company}')
    @classmethod
    def display(cls,newcompany):
        cls.company=newcompany



e1=Employee()
e1.name="Riya"
e1.display("Tesla")
e1.show()
print(Employee.company)
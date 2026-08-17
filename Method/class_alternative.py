# class Students:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def from_string(cls,string):
#         name,salary=string.split("-")
#         return cls(name,int(salary))
# s= Students.from_string("Riya-59999")
# print(s.name)
# print(s.salary)





















class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def form_string(cls,string):
        name,salary=string.split("-")
        return cls(name,int(salary))

e=Employee.form_string("Riya-75000")
print(e.name)
print(e.salary)
        
        
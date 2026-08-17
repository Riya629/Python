class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showdetail(self):
        print(f"Name:{self.name}, Id:{self.id}")


class Developer(Employee):
    def showlanguage(self):
        print("The default language is python")

e=Employee("Riya",21)
e.showdetail()
e2=Developer("sachet",25)
e2.showdetail()
e2.showlanguage()
class Math:
    @staticmethod
    def add(a,b):
        return a+b
print(Math.add(2,3))      #Here we can call the static methods using the class name and object too
# we can call it creating object too
m=Math()
print(m.add(1,2))


#instance variable and class variable
class Employee:
    company="Google"
    def __init__(self,name):
        self.name=name #instance variable
    def display(self):
        print(f'The name of the Employee is {self.name}  and the company name is {self.company} ')
        # print(f"The company is {Employee.company}") we can acces the class variable bybusing the class name in this way

e1=Employee("Riya")
# what if we want to chnage the company of the e1 than
e1.company="Apple"
e1.display()
e2=Employee("Sachet")
#we can change the value by creating the instance variable of the object by doing so the class varaiable isnnot change the instance variable is changed
e2.company="microsoft"
e2.display()
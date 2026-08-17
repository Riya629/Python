#example of public access modifier
# class Employee:
#     def __init__(self):
#         self.name="Riya"
# e=Employee()
# print(e.name)

#example of private access modifier

class student:
    def __init__(self):
        self.__name="Sachet"
s=student()
# print(s.__name) #throw an error beacuse we cannot acess private variable directly we use getter stter of name mangling
print(s._student__name)
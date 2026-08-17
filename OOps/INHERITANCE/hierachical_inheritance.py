class Father:
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(f"The name of father is {self.name}")


class Daughter(Father):
    def __init__(self,name,age):
        Father.__init__(self,name)
        self.age=age
    def show2(self):
        print(f"The name is {self.name} and age is {self.age}")

class son(Father):
    def __init__(self,name,address):
        Father.__init__(self,name)
        self.address=address
    def show3(self):
        print(f"hi iam {self.name}  from{self.address}")


D=Daughter("Riya",20)
D.show2()
D.show1()

s=son("sachet", "Bharatpur")
s.show3()
s.show1()

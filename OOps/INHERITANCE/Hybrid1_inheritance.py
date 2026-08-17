class BaseClass:
    def __init__(self, id):
        self.id = id

    def showid(self):
        print(f"The id is {self.id}")


class Derived1(BaseClass):
    def __init__(self, id, name):
        BaseClass.__init__(self,id)
        self.name = name

    def showname(self):
        print(f"The name is {self.name} and id is {self.id}")


class Derived2(BaseClass):
    def __init__(self, id, age):
        super().__init__(id)
        self.age = age

    def showage(self):
        print(f"The id is {self.id} and age is {self.age}")


class Derived3(Derived1, Derived2):
    def __init__(self, id, name, age, address):
        Derived1.__init__(self,id, name)
        self.age = age
        self.address = address

    def showdetail(self):
        print(f"The is is {self.id}")
        print(f"The name is {self.name}")
        print(f"The age is {self.age}")
        print(f"The address is {self.address}")


d3 = Derived3(1, "Riya", 20, "Bharatpur-12")
d3.showid()
d3.showname()
d3.showage()
d3.showdetail()



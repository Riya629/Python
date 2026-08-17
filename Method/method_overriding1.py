# Method overriding example
class Animals:
    def sound(self):
        print("Animal makes sound")


class Dog(Animals):
    def sound(self):
        print("Dog barks")


d = Dog()
d.sound()


class students:
    def display(self, name, id):
        self.name = name
        self.id = id


class bcastudents(students):
    def display(self, name, id):
        self.name = name
        self.id = id
        print(f"{self.name} and {self.id}")


b = bcastudents()
b.display("Riya", 1)


class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 *super().area()


c = circle(3)
print(c.area())











class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y

class square(shape):
    # def __init__(self,length):
    #     self.length=length  we can do in this way tooo
    def __init__(self,length):
        self.length=length
        super().__init__(length,length)
    def area(self):
        return super().area()
        
    # def area(self):
        # return self.length*self.length we can do in this way to

s=square(2)
print(s.area())
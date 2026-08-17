class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass
# a=Animal()
# a.sound()
d=Dog()
d.sound()


class Vehicles:
    def start(self):
        print("Vehicle started")
class car(Vehicles):
    def music(self):
        print("Music started")

c=car()
c.start()
c.music()
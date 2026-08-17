# Example of single inheritance using the super keyword
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makesound(self):
        print("Animals makes sound")


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
        # animal().__init__(self,name,species) we can use parent class name also but we must used self as it doenot handle current object automatically
        # self.breed=breed

    def makesound(self):
        print("Dogs barks")

    def info(self):
        return f"{self.name} {self.species} {self.breed}"


d = Dog("Tommy", "Dog", "German Shepherd")
d.makesound()
print(d.info())
a = Animal("Dog", "Dog")
a.makesound()

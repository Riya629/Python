# Assignment to implement single inheritance


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makesound(self):
        print("sound made by animals")


class cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def makesound(self):
        print("cat make sound meow meow!")

    def info(self):
        print(f"{self.name} {self.species} {self.breed}")


c = cat("Luna", "Cat", "Persian")
c.makesound()
c.info()

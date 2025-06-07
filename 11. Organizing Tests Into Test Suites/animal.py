class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "unknown"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat")

    def make_sound(self):
        return "meow"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog")

    def make_sound(self):
        return "woof"

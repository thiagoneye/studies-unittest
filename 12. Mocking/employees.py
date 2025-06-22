import random


class Programmer:
    def __init__(self):
        self.tech_names = set()

    def add_tech(self, tech_name):
        name = tech_name.lower()
        if name not in self.tech_names:
            self.tech_names.add(name)
        return self

    def get_random_tech(self):
        if not self.tech_names:
            raise ValueError("No technologies added yet")
        return random.choice(list(self.tech_names))

    def display_random_tech(self):
        return f"Technology name: {self.get_random_tech()}"

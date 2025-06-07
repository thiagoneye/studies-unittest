import random
from unittest.mock import patch


class Programmer:
    def __init__(self):
        self.tech_names = []

    def add_tech(self, tech_name):
        name = tech_name.lower()
        if name not in self.tech_names:
            self.tech_names.append(name)
        return self

    def get_random_tech(self):
        return random.choice(self.tech_names)


if __name__ == "__main__":

    programmer = Programmer()
    programmer.add_tech("python")
    programmer.add_tech("java")
    programmer.add_tech("sql")
    programmer.add_tech("aws")
    programmer.add_tech("django")

    @patch("random.choice")
    def test_get_random_tech(mock_random):
        mock_random.return_value = "c++"
        return programmer.get_random_tech()

    print(test_get_random_tech())

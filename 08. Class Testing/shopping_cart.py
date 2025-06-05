class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_price(self):
        return sum(item.get_price() for item in self.items)

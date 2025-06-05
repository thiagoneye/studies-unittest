import uuid


class Product:
    def __init__(self, product_name, price):
        self._product_id = self._generate_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    def _generate_id(self):
        return str(uuid.uuid4().fields[-1])[:6]

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        raise AttributeError("product_id cannot be changed")


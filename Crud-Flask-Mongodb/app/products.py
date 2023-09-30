class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def toCollection(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

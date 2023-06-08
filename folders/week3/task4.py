class Clothing():
    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    def display_info(self):
        print("Name:", self.name)
        print("Size:", self.size)
        print("Color:", self.color)
        print("Price:", self.price)


class Shirt(Clothing):
    def __init__(self, name, size, color, price, type):
        super().__init__(name, size, color, price)
        self.type = type

    def display_info(self):
        super().display_info()
        print("Type:", self.type)


class Pants(Clothing):
    def __init__(self, name, size, color, price, length):
        super().__init__(name, size, color, price)
        self.length = length

    def display_info(self):
        super().display_info()
        print("Length:", self.length)


shirt = Shirt("T-Shirt", "L", "White", 54.0, "Casual")
shirt.display_info()

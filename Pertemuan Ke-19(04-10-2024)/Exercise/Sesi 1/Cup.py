class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity
        self.space = size - quantity

    def fill(self, fill_quantity: int):
        if self.quantity + fill_quantity > self.size:
            return "Not enough space!"
        else:
            self.quantity += fill_quantity
            self.space = self.size - self.quantity
        return self.quantity

    def status(self):
        return self.space

cup = Cup(100, 50)
print(cup.status())  # Output: 50
cup.fill(40)
cup.fill(20)
print(cup.status())
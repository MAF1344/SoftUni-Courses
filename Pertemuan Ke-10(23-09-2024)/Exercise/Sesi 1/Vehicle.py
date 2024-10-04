class Vehicle:
    def __init__(self, type: str, model: str, price: float):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: float, owner: str):
        if self.owner is not None:
            return "Car already sold"
        if money >= self.price:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"

# Test Code
# Test Case 1: Membeli kendaraan dengan cukup uang
vehicle1 = Vehicle("Car", "Model X", 50000)
print(vehicle1.buy(60000, "Alice"))  # Harus berhasil membeli dan mencetak pesan perubahan

# Test Case 2: Membeli kendaraan yang sudah terjual
vehicle2 = Vehicle("Bike", "Model Y", 20000)
vehicle2.buy(30000, "Bob")
print(vehicle2.buy(10000, "Charlie"))  # Harus mencetak "Car already sold"

# Test Case 3: Membeli kendaraan dengan uang tidak cukup
vehicle3 = Vehicle("Truck", "Model Z", 40000)
print(vehicle3.buy(30000, "David"))  # Harus mencetak "Sorry, not enough money"

# Test Case 4: Menjual kendaraan yang sudah dimiliki
vehicle4 = Vehicle("Van", "Model A", 70000)
vehicle4.buy(80000, "Eve")
vehicle4.sell()
print(vehicle4)  # Harus mencetak bahwa kendaraan tersedia untuk dijual

# Test Case 5: Menjual kendaraan yang tidak memiliki pemilik
vehicle5 = Vehicle("SUV", "Model B", 90000)
print(vehicle5.sell())  # Harus mencetak "Vehicle has no owner"


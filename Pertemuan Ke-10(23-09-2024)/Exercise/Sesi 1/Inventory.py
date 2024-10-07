class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity  # Private attribute
        self.items = []  # List untuk menyimpan item

    def add_item(self, item: str):
        # Menambahkan item jika masih ada ruang
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        # Mengembalikan nilai kapasitas total
        return self.__capacity

    def __repr__(self):
        # Menghitung kapasitas yang tersisa
        left_capacity = self.__capacity - len(self.items)
        # Mengembalikan format string sesuai yang diminta
        return f"Items: {', '.join(self.items)}.\nCapacity left: {left_capacity}"

# Test Code
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))  # "not enough room in the inventory"
print(inventory.get_capacity())  # 2
print(inventory)

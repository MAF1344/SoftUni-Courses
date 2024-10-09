

from ..food import Meat
from ..food import Vegetable
from ..food import Fruit
from .animal import Mammal

class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if isinstance(food, (Vegetable, Fruit)):
            self.weight += food.quantity * 0.10
            self.food_eaten += food.quantity
        else:
            return f"Mouse does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.40
            self.food_eaten += food.quantity
        else:
            return f"Dog does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Dog [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if isinstance(food, (Vegetable, Meat)):
            self.weight += food.quantity * 0.30
            self.food_eaten += food.quantity
        else:
            return f"Cat does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Cat [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 1.00
            self.food_eaten += food.quantity
        else:
            return f"Tiger does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Tiger [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
from project.animals.birds import Owl
from project.food import Meat
from project.food import Vegetable
from project.animals.birds import Hen
from project.food import Fruit
from project.animals.mammals import Mouse
from project.animals.mammals import Dog
from project.animals.mammals import Cat
from project.animals.mammals import Tiger
# Test Code Example
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

from .dough import Dough
from .topping import Topping

class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        if not name:
            raise ValueError("The name cannot be an empty string")
        if dough is None:
            raise ValueError("You should add dough to the pizza")
        if max_number_of_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__name = name
        self.__dough = dough
        self.__max_number_of_toppings = max_number_of_toppings
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings(self):
        return self.__toppings

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    def add_topping(self, topping: Topping):
        if len(self.__toppings) >= self.__max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.__toppings:
            self.__toppings[topping.topping_type] += topping.weight
        else:
            self.__toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return self.__dough.weight + sum(self.__toppings.values())

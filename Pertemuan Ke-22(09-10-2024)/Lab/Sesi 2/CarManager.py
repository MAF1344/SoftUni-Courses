class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest

class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Corolla", 5, 50)

    def test_constructor_initializes_correctly(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Corolla")
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 50)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_setter_raises_error_if_null_or_empty(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_model_setter_raises_error_if_null_or_empty(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_setter_raises_error_if_zero_or_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_setter_raises_error_if_zero_or_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_setter_raises_error_if_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -10
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_increases_fuel_amount(self):
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 20)

    def test_refuel_does_not_exceed_fuel_capacity(self):
        self.car.refuel(60)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_refuel_with_zero_or_negative_raises_error(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.refuel(-10)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_drive_reduces_fuel_amount(self):
        self.car.refuel(50)
        self.car.drive(100)  # Should use 5 liters (100 km / 100 * 5 consumption)
        self.assertEqual(self.car.fuel_amount, 45)

    def test_drive_without_enough_fuel_raises_error(self):
        self.car.refuel(5)
        with self.assertRaises(Exception) as context:
            self.car.drive(200)  # Needs 10 liters for 200 km
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")

    def test_drive_exactly_with_enough_fuel(self):
        self.car.refuel(5)
        self.car.drive(100)  # Uses exactly 5 liters
        self.assertEqual(self.car.fuel_amount, 0)


if __name__ == "__main__":
    unittest.main()

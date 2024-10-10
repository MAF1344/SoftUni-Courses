class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


import unittest

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("John", 100, 10)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual(self.worker.name, "John")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 10)

    def test_worker_energy_is_incremented_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_worker_raises_exception_if_energy_is_not_enough(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), "Not enough energy.")

    def test_worker_money_increased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_worker_energy_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_get_info_returns_correct_string(self):
        expected_output = "John has saved 0 money."
        self.assertEqual(self.worker.get_info(), expected_output)


if __name__ == "__main__":
    unittest.main()

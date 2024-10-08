from .animal import Animal
from .lion import Lion
from .tiger import Tiger
from .cheetah import Cheetah
from .worker import Worker
from .keeper import Keeper
from .caretaker import Caretaker
from .vet import Vet

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_cost = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= total_care_cost:
            self.__budget -= total_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]
        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:",
            *lions,
            f"----- {len(tigers)} Tigers:",
            *tigers,
            f"----- {len(cheetahs)} Cheetahs:",
            *cheetahs,
        ]
        return "\n".join(str(r) for r in result)

    def workers_status(self):
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]
        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(keepers)} Keepers:",
            *keepers,
            f"----- {len(caretakers)} Caretakers:",
            *caretakers,
            f"----- {len(vets)} Vets:",
            *vets,
        ]
        return "\n".join(str(r) for r in result)

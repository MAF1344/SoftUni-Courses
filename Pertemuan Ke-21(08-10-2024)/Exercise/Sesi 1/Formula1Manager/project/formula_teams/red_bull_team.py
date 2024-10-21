from .formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def __init__(self, budget: int) -> object:
        super().__init__(budget)

    @property
    def expenses(self):
        return 250_000

    @property
    def name(self):
        return "Red Bull"

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = self.teams[self.name].get(race_pos, 0) - self.expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
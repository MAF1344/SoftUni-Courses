class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def heal(self, amount):
        self.health += amount

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0  # Set health to 0 if it goes below 0
            return f"{self.name} was defeated"
        return None  # Return None if hero is not defeated
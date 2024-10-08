class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        if not flour_type:
            raise ValueError("The flour type cannot be an empty string")
        if not baking_technique:
            raise ValueError("The baking technique cannot be an empty string")
        if weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @property
    def weight(self):
        return self.__weight

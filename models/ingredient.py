from dataclasses import dataclass
from decimal import Decimal
from numbers import Number

@dataclass
class Ingredient:
    id: int
    name: str
    purchasing_cost: float
    unit_amount: float
    unit_of_measure: str

    def __init__(self, id: int, name: str, purchasing_cost: float, unit_amount: float, unit_of_measure: str):
        
        self.id = id
        self.name = name
        self.purchasing_cost = purchasing_cost
        self.unit_amount = unit_amount
        self.unit_of_measure = unit_of_measure
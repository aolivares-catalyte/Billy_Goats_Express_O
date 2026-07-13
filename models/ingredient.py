from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Ingredient:
    name: str
    purchasing_cost: float
    unit_amount: float
    unit_of_measure: str

    def __init__(self, name: str, purchasing_cost: float, unit_amount: float, unit_of_measure: str):
        
        self.name = name
        self.purchasing_cost = purchasing_cost
        self.unit_amount = unit_amount
        self.unit_of_measure = unit_of_measure
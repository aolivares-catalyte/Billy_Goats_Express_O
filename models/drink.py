from dataclasses import dataclass
from decimal import Decimal
from ingredient import Ingredient

@dataclass
class Drink:
    name: str
    ingredients: list[Ingredient]
    cost_to_produce: Decimal
    markup_percentage: Decimal
    sale_price: Decimal

    def __init__(self, name: str, ingredients: list[Ingredient], cost_to_produce: Decimal, markup_percentage: Decimal):
        self.name = name
        self.ingredients = ingredients
        self.cost_to_produce = cost_to_produce
        self.markup_percentage = markup_percentage
        self.sale_price = cost_to_produce * (1 + markup_percentage)

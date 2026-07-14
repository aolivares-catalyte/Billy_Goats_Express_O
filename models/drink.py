from dataclasses import dataclass
from decimal import Decimal
from models.ingredient import Ingredient

@dataclass
class Drink:
    id: int
    name: str
    ingredients: list[Ingredient]
    cost_to_produce: Decimal
    markup_percentage: Decimal
    sale_price: Decimal

    def __init__(self, id: int, name: str, ingredients: list[Ingredient], cost_to_produce: Decimal, markup_percentage: Decimal):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.cost_to_produce = cost_to_produce
        self.markup_percentage = markup_percentage
        self.sale_price = (cost_to_produce * (Decimal("1") + markup_percentage)).quantize(Decimal("0.01"))

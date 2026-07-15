from dataclasses import dataclass
from decimal import Decimal
from models.ingredient import Ingredient

@dataclass
class Drink:
    """Represents a drink available for purchase.

    This is a plain data container. Invariants are enforced by DrinkService.

    Attributes:
        id: A unique integer ID.
        name: The drink's name.
        ingredients: The list of ingredients the drink is made from.
        cost_to_produce: The cost to prepare the drink.
        markup_percentage: The markup percentage, expressed as a Decimal >= 1.0
            (a 30% markup is Decimal("1.30")).
        sale_price: The sale price, which should be equal to
            cost_to_produce * markup_percentage; not validated here.
    """
    id: int
    name: str
    ingredients: list[Ingredient]
    cost_to_produce: Decimal
    markup_percentage: Decimal
    sale_price: Decimal | None = None

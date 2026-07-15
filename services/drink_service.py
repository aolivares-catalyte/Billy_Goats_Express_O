from models.drink import Drink
from repositories.drink_repository import DrinkRepository
from exceptions import DuplicateDrinkError

class DrinkService:
    def __init__(self, repository: DrinkRepository) -> None:
        self._repository = repository

    def create_drink(self, drink: Drink) -> Drink:
        if self._repository.get_by_name(drink.name) is not None:
            msg = f"Drink {drink.name} already exists"
            raise DuplicateDrinkError(msg)
        elif self._repository.get_by_id(drink.id) is not None:
            msg = f"Drink {drink.id} already exists"
            raise DuplicateDrinkError(msg)
        else:
            # calculate the sale_price
            drink.sale_price = drink.cost_to_produce * drink.markup_percentage
            return self._repository.add(drink)

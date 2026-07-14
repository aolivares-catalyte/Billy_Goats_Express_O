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
        return self._repository.add(drink)

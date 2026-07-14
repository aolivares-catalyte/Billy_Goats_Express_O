import pytest
from exceptions import DuplicateDrinkError
from models.drink import Drink, Ingredient
from repositories.drink_repository import DrinkRepository
from services.drink_service import DrinkService
from decimal import Decimal

def test_duplicate_drink_should_raise_DuplicateDrinkError(beans, water, sample_drink_service):
    with pytest.raises(DuplicateDrinkError):
        markup = Decimal("0.30")
        drink = Drink(5, "Americano", [beans, water], Decimal("5.25"), markup)
        sample_drink_service.create_drink(drink)

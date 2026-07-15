import pytest
from exceptions import DuplicateDrinkError
from models.drink import Drink, Ingredient
from repositories.drink_repository import DrinkRepository
from services.drink_service import DrinkService
from decimal import Decimal

def test_duplicate_drink_name_should_raise_DuplicateDrinkError(beans, water, sample_drink_service):
    with pytest.raises(DuplicateDrinkError):
        markup = Decimal("0.30")
        drink = Drink(5, "Americano", [beans, water], Decimal("5.25"), markup)
        sample_drink_service.create_drink(drink)

def test_duplicate_drink_id_should_raise_DuplicateDrinkError(black_tea_leaves, water, sample_drink_service):
    with pytest.raises(DuplicateDrinkError):
        markup = Decimal("0.30")
        drink = Drink(1, "Black Tea", [black_tea_leaves, water], Decimal("5.25"), markup)
        sample_drink_service.create_drink(drink)

@pytest.mark.parametrize("input, expected", [
    ([1, "Americano", [], Decimal("5.60"), Decimal("1.30")], Decimal("7.28")),
    ([2, "Vanilla Latte", [], Decimal("7.60"), Decimal("1.25")], Decimal("9.50")),
])
def test_sale_price_should_be_calculated_from_cost_to_produce_and_markup_percentage(input, expected):
    drink_service = DrinkService(DrinkRepository())
    drink = Drink(*input)
    drink_service.create_drink(drink)
    assert drink.sale_price == expected

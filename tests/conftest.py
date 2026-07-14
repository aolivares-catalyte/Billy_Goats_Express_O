from decimal import Decimal
import pytest

from models.drink import Drink
from models.ingredient import Ingredient
from repositories.drink_repository import DrinkRepository
from services.drink_service import DrinkService

@pytest.fixture
def beans() -> Ingredient:
    return Ingredient(1, "Coffee Beans", Decimal("2.50"), 14.0, "g")

@pytest.fixture
def water() -> Ingredient:
    return Ingredient(2, "Water", Decimal("0.01"), 250.0, "g")

@pytest.fixture
def milk() -> Ingredient:
    return Ingredient(3, "Milk", Decimal("1.25"), 250.0, "g")

@pytest.fixture
def black_tea_leaves() -> Ingredient:
    return Ingredient(4, "Black Tea Leaves", Decimal("3.50"), 10.0, "g")

@pytest.fixture
def americano(beans, water) -> Drink:
    markup = Decimal("0.25")
    return Drink(1, "Americano", [beans, water], Decimal("3.00"), markup)

@pytest.fixture
def latte(beans, water, milk) -> Drink:
    markup = Decimal("0.25")
    return Drink(2, "Latte", [beans, water, milk], Decimal("5.00"), markup)

@pytest.fixture
def sample_drink_service(americano, latte):
    repo = DrinkRepository()
    repo.add(americano)
    repo.add(latte)
    return DrinkService(repo)

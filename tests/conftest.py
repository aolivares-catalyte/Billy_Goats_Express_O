from decimal import Decimal
import pytest

from models.customer import Customer
from models.drink import Drink
from models.ingredient import Ingredient
from repositories.customer_repository import CustomerRepository
from models.baked_good import BakedGood
from models.customer import Customer
from models.purchase import Purchase
from repositories.drink_repository import DrinkRepository
from services.customer_service import CustomerService
from services.drink_service import DrinkService

# Customers

@pytest.fixture
def marcus():
    return Customer(1, "Marcus Whitfield", "marcus.whitfield@example.com", Decimal("0.0"))

@pytest.fixture
def priya():
    return Customer(2, "Priya Chandrasekaran", "priya.chandrasekaran@example.com", Decimal("560.27"))

# Ingredients

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

# Drinks

@pytest.fixture
def americano(beans, water) -> Drink:
    markup = Decimal("0.25")
    return Drink(1, "Americano", [beans, water], Decimal("3.00"), markup)

@pytest.fixture
def latte(beans, water, milk) -> Drink:
    markup = Decimal("0.25")
    return Drink(2, "Latte", [beans, water, milk], Decimal("5.00"), markup)

# Services

@pytest.fixture
def sample_customer_service(marcus, priya):
    repo = CustomerRepository()
    repo.add(marcus)
    repo.add(priya)
    return CustomerService(repo)

@pytest.fixture
def sample_drink_service(americano, latte):
    repo = DrinkRepository()
    repo.add(americano)
    repo.add(latte)
    return DrinkService(repo)

@pytest.fixture
def blueberry_muffin()->BakedGood:
    return BakedGood(1,"blueberry_muffin",1.50,2.00,"Blue Farms",["Wheat","Eggs","Milk","Soy"])

@pytest.fixture
def allen()->Customer:
    return Customer(99,"Allen","aolivares1042@gmail.com",2000.00)

@pytest.ficture
def allen_purchase()->Purchase:
    return Purchase((120,datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),[blueberry_muffin(),latte()],Customer(99,"Allen","aolivares1042@gmail.com",2000.00)))
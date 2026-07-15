from decimal import Decimal
import pytest
from datetime import datetime, timezone

# from models.customer import Customer
# from models.drink import Drink
# from models.ingredient import Ingredient
# from repositories.customer_repository import CustomerRepository
# from repositories.purchase_repository import PurchaseRepository
from repositories.baked_good_repository import BakedGoodRepository
from models.baked_good import BakedGood
# from models.customer import Customer
# from models.purchase import Purchase
# from repositories.drink_repository import DrinkRepository
# from services.customer_service import CustomerService
# from services.drink_service import DrinkService
from services.baked_good_service import BakedGoodService

# Customers

# @pytest.fixture
# def marcus():
#     return Customer(1, "Marcus Whitfield", "marcus.whitfield@example.com")

# @pytest.fixture
# def priya():
#     return Customer(2, "Priya Chandrasekaran", "priya.chandrasekaran@example.com", Decimal("560.27"))

# @pytest.fixture
# def diego():
#     return Customer(3, "Diego Fernandez", "diego.fernandez@example.com", Decimal("1067.48"))
# @pytest.fixture
# def allen()->Customer:
#     return Customer(99,"Allen","aolivares1042@gmail.com",Decimal("2000.00"))



# Ingredients

# @pytest.fixture
# def beans() -> Ingredient:
#     return Ingredient(1, "Coffee Beans", Decimal("2.50"), 14.0, "g")

# @pytest.fixture
# def water() -> Ingredient:
#     return Ingredient(2, "Water", Decimal("0.01"), 250.0, "g")

# @pytest.fixture
# def milk() -> Ingredient:
#     return Ingredient(3, "Milk", Decimal("1.25"), 250.0, "g")

# @pytest.fixture
# def black_tea_leaves() -> Ingredient:
#     return Ingredient(4, "Black Tea Leaves", Decimal("3.50"), 10.0, "g")

# # Drinks

# @pytest.fixture
# def americano(beans, water) -> Drink:
#     markup = Decimal("0.25")
#     return Drink(1, "Americano", [beans, water], Decimal("3.00"), markup)

# @pytest.fixture
# def latte(beans, water, milk) -> Drink:
#     markup = Decimal("0.25")
#     return Drink(2, "Latte", [beans, water, milk], Decimal("5.00"), markup)

# @pytest.fixture
# def black_tea(black_tea_leaves, water) -> Drink:
#     markup = Decimal("0.17")
#     return Drink(3, "Black Tea", [black_tea_leaves, water], Decimal("1.50"), markup)

# # Services

# @pytest.fixture
# def sample_customer_service(marcus, priya):
#     repo = CustomerRepository()
#     repo.add(marcus)
#     repo.add(priya)
#     return CustomerService(repo)

# @pytest.fixture
# def sample_drink_service(americano, latte):
#     repo = DrinkRepository()
#     repo.add(americano)
#     repo.add(latte)
#     return DrinkService(repo)

# # Repositories

# @pytest.fixture
# def sample_customer_repository(marcus, priya):
#     repo = CustomerRepository()
#     repo.add(marcus)
#     repo.add(priya)
#     return repo

# @pytest.fixture
# def sample_drink_repository(americano, latte):
#     repo = DrinkRepository()
#     repo.add(americano)
#     repo.add(latte)
#     return repo

# @pytest.fixture
# def sample_purchase_repository(allen_purchase,marcus_purchase,priya_purchase):
#     repo=PurchaseRepository()
#     repo.add(allen_purchase)
#     repo.add(marcus_purchase)
#     repo.add(priya_purchase)
#     return repo

# @pytest.fixture
# def second__sample_purchase_repository(allen_purchase,marcus_purchase,diego_purchase):
#     repo=PurchaseRepository()
#     repo.add(allen_purchase)
#     repo.add(marcus_purchase)
#     repo.add(diego_purchase)
#     return repo



# @pytest.fixture
# def complete_purchase_repository(allen_purchase,marcus_purchase,priya_purchase,diego_purchase):
#     repo=PurchaseRepository()
#     repo.add(allen_purchase)
#     repo.add(marcus_purchase)
#     repo.add(priya_purchase)
#     repo.add(diego_purchase)
#     return repo
    

#Baked Good

@pytest.fixture
def blueberry_muffin()->BakedGood:
    return BakedGood(11,"blueberry_muffin",Decimal("1.50"),Decimal("2.00"),"Blue Farms",["Wheat","Eggs","Milk","Soy"])
def banana_nut_muffin()->BakedGood:
    return BakedGood(12,"banana_nut_muffin",Decimal("1.50"),Decimal("2.00"),"banana Farms",["Wheat","Eggs","Milk","Soy"])
@pytest.fixture
def baked_good_repository():
    return BakedGoodRepository()
@pytest.fixture
def baked_good_service(baked_good_repository):
    return BakedGoodService(baked_good_repository)
@pytest.fixture
def sample_baked_good_repository(blueberry_muffin) -> BakedGoodRepository:
    repo = BakedGoodRepository()
    repo.add(blueberry_muffin)
    return repo


#Purchase 
# @pytest.fixture
# def allen_purchase(blueberry_muffin,latte,allen)->Purchase:
#     d=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
#     return Purchase(120,[blueberry_muffin,latte],allen,d)
# @pytest.fixture
# def marcus_purchase(marcus, americano, blueberry_muffin) -> Purchase:
#     """Marcus buys a simple coffee and a muffin."""
#     d = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
#     return Purchase(121, [americano, blueberry_muffin], marcus, d)

# @pytest.fixture
# def priya_purchase(priya, black_tea) -> Purchase:
#     """Priya buys two black teas."""
#     d = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
#     return Purchase(122, [black_tea, black_tea], priya, d)

# @pytest.fixture
# def diego_purchase(diego, latte) -> Purchase:
#     """Diego buys a single latte."""
#     d = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
#     return Purchase(123, [latte], diego, d)


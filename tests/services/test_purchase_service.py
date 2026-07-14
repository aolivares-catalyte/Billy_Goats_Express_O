from models.purchase import Purchase
from models.customer import Customer
from models.drink import Drink
from models.ingredient import Ingredient
from repositories.purchase_repository import PurchaseRepository
from services.purchase_service import PurchaseService
from decimal import Decimal

from tests.conftest import allen_purchase

def test_purchase_model(allen_purchase):
    assert allen_purchase.id == 120 



#def test_create_purchase():
    #assert PurchaseService.create_purchase(,allen_purchase) ==allen_purchase
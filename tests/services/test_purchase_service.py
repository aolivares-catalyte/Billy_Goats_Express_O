from models.purchase import Purchase
from models.customer import Customer
from models.drink import Drink
from models.ingredient import Ingredient
from repositories.purchase_repository import PurchaseRepository
from services.purchase_service import PurchaseService
from decimal import Decimal

from tests.conftest import allen_purchase, sample_purchase_repository, diego_purchase,complete_purchase_repository,second__sample_purchase_repository

def test_purchase_model(allen_purchase):
    assert allen_purchase.id == 120 

def test_purchase_repository_addall(sample_purchase_repository,diego_purchase,complete_purchase_repository):
    sample_purchase_repository.add(diego_purchase)
    assert sample_purchase_repository.get_all() == complete_purchase_repository.get_all()

def test_purchase_repository_get_by_id(complete_purchase_repository,allen_purchase):
    n=complete_purchase_repository.get_by_id(120)
    assert n==allen_purchase

def test_purchase_repository_update(second__sample_purchase_repository, diego_purchase):

    updated_purchase = second__sample_purchase_repository.update(123, diego_purchase)
    fetched_purchase = second__sample_purchase_repository.get_by_id(123)
    assert fetched_purchase == diego_purchase





#def test_create_purchase():
    #assert PurchaseService.create_purchase(,allen_purchase) ==allen_purchase
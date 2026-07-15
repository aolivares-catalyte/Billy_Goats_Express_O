# from models.purchase import Purchase
# from models.customer import Customer
# from models.drink import Drink
# from models.ingredient import Ingredient
# from repositories.purchase_repository import PurchaseRepository
# from services.purchase_service import PurchaseService
# from decimal import Decimal
# from datetime import datetime, timezone
# import pytest
# from exceptions import DuplicatePurchaseError,IncorrectDateFormat

# from tests.conftest import allen_purchase, sample_purchase_repository, diego_purchase,complete_purchase_repository,second__sample_purchase_repository, sample_purchase_service, allen

# def test_purchase_model(allen_purchase):
#     assert allen_purchase.id == 120 

# def test_purchase_repository_addall(sample_purchase_repository,diego_purchase,complete_purchase_repository):
#     sample_purchase_repository.add(diego_purchase)
#     assert sample_purchase_repository.get_all() == complete_purchase_repository.get_all()

# def test_purchase_repository_get_by_id(complete_purchase_repository,allen_purchase):
#     n=complete_purchase_repository.get_by_id(120)
#     assert n==allen_purchase

# def test_purchase_repository_update(second__sample_purchase_repository, diego_purchase):

#     updated_purchase = second__sample_purchase_repository.update(123, diego_purchase)
#     fetched_purchase = second__sample_purchase_repository.get_by_id(123)
#     assert fetched_purchase == diego_purchase

# def test_purchase_repository_delete(complete_purchase_repository):
#     deleted_purchase = complete_purchase_repository.delete(120)
#     fetched_purchase = complete_purchase_repository.get_by_id(120)
#     assert fetched_purchase == None

# def test_duplicate_purchase_id_should_raise_DuplicatepurchaseError(sample_purchase_service,blueberry_muffin,latte,allen):
#     with pytest.raises(DuplicatePurchaseError):
#         d=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
#         purchase=Purchase(120,[blueberry_muffin,latte],allen,d)
#         sample_purchase_service.create_purchase(purchase)

# def test_incorrect_purchase_date_raise_error(sample_purchase_service,blueberry_muffin,latte):
#     with pytest.raises(IncorrectDateFormat):
#         d="12-31-2099"
#         Alex=Customer(7,"Alex","ahernandez@gmail.com",Decimal("900.00"))
#         purchase=Purchase(130,[blueberry_muffin,latte],Alex,d)
#         sample_purchase_service.create_purchase(purchase)

# def test_total_cost_creating_purchase(blueberry_muffin,latte):
#     purchaseService = PurchaseService(PurchaseRepository())
#     d=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
#     Alex=Customer(7,"Alex","ahernandez@gmail.com",Decimal("900.00"))
#     purchase=Purchase(130,[blueberry_muffin,latte],Alex,d)
#     ps=purchaseService.create_purchase(purchase)
#     x=ps.total_cost
#     exact=Decimal("7.78")
#     assert x == exact

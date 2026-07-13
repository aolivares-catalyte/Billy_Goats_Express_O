from repositories.purchase_repository import PurchaseRepository
from models.purchase import Purchase
from exceptions import DuplicatePurchaseError

class PurchaseService:
    def __init__(self, repository: PurchaseRepository):
        self._repository = repository

    def create_purchase(self, purchase: Purchase) -> Purchase:
        if self._repository.get_by_id(Purchase.id) is not None:
            raise DuplicatePurchaseError(f"Purchase '{Purchase.id}' already exists.")
        return self._repository.add(Purchase)

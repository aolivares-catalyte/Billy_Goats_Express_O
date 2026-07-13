from repositories.purchase_repository import PurchaseRepository
from models.purchase import Purchase
from exceptions import DuplicatePurchaseError,Incorrect_date_format
from datetime import datetime

class PurchaseService:
    def __init__(self, repository: PurchaseRepository):
        self._repository = repository

    def create_purchase(self, purchase: Purchase) -> Purchase:
        if self._repository.get_by_id(purchase.id) is not None:
            raise DuplicatePurchaseError(f"Purchase '{purchase.id}' already exists.")
        correct_format = "%Y-%m-%d %H:%M:%S UTC"
        date_string=self._repository.get_by_id(purchase.id).timestamp
        try:
            datetime.strptime(date_string, correct_format)
        except ValueError:
            raise Incorrect_date_format(f"Timestamp {date_string} is not in the right format")
        return self._repository.add(purchase)

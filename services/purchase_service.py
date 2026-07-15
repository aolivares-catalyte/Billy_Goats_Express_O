from repositories.purchase_repository import PurchaseRepository
from models.purchase import Purchase
from models.drink import Drink
from models.baked_good import BakedGood
from exceptions import DuplicatePurchaseError,IncorrectDateFormat
from datetime import datetime, timezone

class PurchaseService:
    def __init__(self, repository: PurchaseRepository):
        self._repository = repository

    def create_purchase(self, purchase: Purchase) -> Purchase:
        if self._repository.get_by_id(purchase.id) is not None:
            raise DuplicatePurchaseError(f"Purchase '{purchase.id}' already exists.")
        date_string= purchase.timestamp
        correct_format = "%Y-%m-%d %H:%M:%S UTC"
        try:
            datetime.strptime(date_string, correct_format)
        except (TypeError,ValueError):
            raise IncorrectDateFormat(f"Timestamp {date_string} is not in the right format")
        return self._repository.add(purchase)

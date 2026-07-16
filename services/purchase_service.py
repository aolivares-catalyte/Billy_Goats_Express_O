from repositories.purchase_repository import PurchaseRepository
from models.purchase import Purchase
from models.drink import Drink
from models.baked_good import BakedGood
from exceptions import DuplicatePurchaseError,IncorrectDateFormat
from datetime import datetime, timezone
from collections import Counter

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
        purchase.total_cost
        return self._repository.add(purchase)
    def get_all_purchases(self):
        return self._repository.get_all()
    

    def get_all_purchases_by_date(self,date):
        correct_date=[]
        correct_format = "%Y-%m-%d %H:%M:%S UTC"
        try:
            datetime.strptime(date, correct_format)
        except (TypeError,ValueError):
            raise IncorrectDateFormat(f"Timestamp {date} is not in the right format")
        for purchase in self._repository.get_all():
            if purchase.timestamp ==date:
                correct_date.append(purchase)
        return correct_date
    def get_all_purchases_by_date(self, date: str):
        correct_date = []
        correct_format = "%Y-%m-%d"
        try:
            datetime.strptime(date, correct_format)
        except (TypeError, ValueError):
            raise IncorrectDateFormat(f"Date {date} is not in the right format. Please use YYYY-MM-DD.")
        for purchase in self._repository.get_all():
            if purchase.timestamp.startswith(date):
                correct_date.append(purchase)
                
        return correct_date
    def get_most_frequent_item(self):
        all_items = []
        x=self._repository.get_all()
        for current_purchase in x:
            for item in current_purchase.items:
                all_items.append(item.name) 
        if not all_items:
            return None
        most_frequent = Counter(all_items).most_common(1)[0][0]
        return most_frequent
    

from models.purchase import Purchase

class PurchaseRepository:
    def __init__(self):
        self._purchases=list[Purchase] = []
    def get_all(self):
        return self._purchases
    def get_by_id(self,id:int):
        return ((p for p in self._purchases if p.id == id), None)
    def add(self, purchase: Purchase) -> Purchase:
        self._purchases.append(purchase)
        return purchase
    def update(self, id: int, purchase: Purchase):
        for p in self._purchases:
            if p.id ==id:
                p = purchase
        return None
    def delete(self, id: int):
        for p in self._purchases:
            if p.id == id:
                self._purchases.remove(p)


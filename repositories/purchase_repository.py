from models.purchase import Purchase

class PurchaseRepository:
    def __init__(self):
        self._purchases=list[Purchase] = []
    def get_all(self):
        return self._purchases
    def get_by_id(self,name:str):
        return ((p for p in self._purchases if p.name == name), None)
    def add(self, purchase: Purchase) -> Purchase:
        self._purchases.append(purchase)
        return purchase
    def update(self, name: str, purchase: Purchase):
        for p in self._purchases:
            if p.name ==name:
                p = purchase
        return None
    def delete(self, name: str):
        for p in self._purchases:
            if p.name == name:
                self._purchases.remove(p)


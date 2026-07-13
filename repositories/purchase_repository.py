from models.purchase import Purchase

class PurchaseRepository:
    def __init__(self):
        self._purchases=list[Purchase] = []
    def get_all(self) ->list[Purchase]:
        return self._purchases
    def get_by_id(self,id:int) -> Purchase | None:
        return ((p for p in self._purchases if p.id == id), None)
    def add(self, purchase: Purchase) -> Purchase:
        self._purchases.append(purchase)
        return purchase
    def update(self, id: int, purchase: Purchase) ->Purchase|None:
        for ind,p in enumerate(self._purchases):
            if p.id ==id:
                self._purchases[ind] = purchase
                return purchase
            else: 
                return None
    def delete(self, id: int)->bool:
        for p in self._purchases:
            if p.id == id:
                self._purchases.remove(p)
                return True
            else:
                return False


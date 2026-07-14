from models.baked_good import BakedGood

class BakedGoodRepository:
    def __init__(self):
        self.baked_goods: list[BakedGood] = []

    def get_all(self) -> list[BakedGood]:
        return self.baked_goods

    def get_by_id(self, id: int) -> BakedGood | None:
        return next((b for b in self.baked_goods if b.id == id), None)

    def add(self, baked_goods: BakedGood) -> BakedGood:
        self.baked_goods.append(baked_goods)
        return baked_goods

    def update(self, name: str, baked_good: BakedGood) -> BakedGood | None:
        existing = self.get_by_id(name)

        if existing:
            index = self.baked_goods.index(existing)
            self.baked_goods[index] = baked_good
            return baked_good

        return None

    def delete(self, name: str) -> bool:
        baked_good = self.get_by_id(name)

        if baked_good:
            self.baked_goods.remove(baked_good)
            return True

        return False
from models.drink import Drink

class DrinkRepository:
    def __init__(self):
        self._drinks: list[Drink] = []

    def get_all(self):
        return self._drinks

    def get_by_id(self, id: int) -> Drink | None:
        return next((d for d in self._drinks if d.id == id), None)

    def get_by_name(self, name: str) -> Drink | None:
        return next((d for d in self._drinks if d.name == name), None)

    def add(self, drink: Drink) -> Drink:
        self._drinks.append(drink)
        return drink

    def update(self, id: int, drink: Drink) -> Drink | None:
        ix = None
        for i, drink in enumerate(self._drinks):
            if id == drink.id:
                ix = i
        if ix:
            self._drinks[ix] = drink
            return drink
        else:
            return None

    def delete(self, id: int) -> bool:
        ix = None
        for i, drink in enumerate(self._drinks):
            if id == drink.id:
                ix = i
        if ix:
            self._drinks.pop(ix)
            return True
        else:
            return False

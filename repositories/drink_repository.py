from models.drink import Drink

class DrinkRepository:
    def __init__(self):
        self.drinks: list[Drink] = []

    def get_all(self):
        return self.drinks

    def get_by_id(self, id: int) -> Drink | None:
        return next((d for d in self._drinks if d.id == id), None)

    def add(self, drink: Drink) -> Drink:
        self.drinks.append(drink)
        return drink

    def update(self, id: int, drink: Drink) -> Drink | None:
        ix = None
        for i, drink in enumerate(self.drinks):
            if id == drink.id:
                ix = i
        if ix:
            self.drinks[ix] = drink
            return drink
        else:
            return None

    def delete(self, id: int) -> bool:
        ix = None
        for i, drink in enumerate(self.drinks):
            if id == drink.id:
                ix = i
        if ix:
            self.drinks.pop(ix)
            return True
        else:
            return False

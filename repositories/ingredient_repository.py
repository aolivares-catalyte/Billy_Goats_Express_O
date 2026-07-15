from models.ingredient import Ingredient

class IngredientRepository:
    def delete_ingredient(self, id: int) -> bool:
        ix = 0
        for ingredient in self.ingredients:
            if ingredient.id == id:
                self.ingredients.pop(ix)
                return True
            ix = ix + 1

        return False
    def add(self, ingredient: Ingredient) -> Ingredient:
        self.ingredients.append(ingredient)
   
        return ingredient
    def get_cost(self, id: int) -> float | None:
        ingredient = self.get_by_id(id)
        if ingredient is not None:
            return ingredient.purchasing_cost
    
        return None
    def get_total_cost(self) -> float:
        total = 0
        for ingredient in self.ingredients:
            total += ingredient.purchasing_cost

        return total
    def update(self, id: int, ingredient: Ingredient) -> Ingredient | None:
        ix = 0
        for current_ingredient in self.ingredients:
            if current_ingredient.id == id:
                self.ingredients[ix] = ingredient
                return ingredient
            ix = ix + 1

        return None
    def get_by_id(self, id: int) -> Ingredient | None:
        for ingredient in self.ingredients:
            if ingredient.id == id:
                return ingredient
        
        return None
    def get_by_name(self, name: str) -> Ingredient | None:
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient

        return None

from models.ingredient import Ingredient
from repositories.ingredient_repository import IngredientRepository
from exceptions import IngredientNotFoundError, DuplicateIngredientError

class IngredientService:
    def __init__(self, repository: IngredientRepository):
        self.repository = repository

    def add_ingredient(self, ingredient: Ingredient) -> Ingredient:
        existing = self.repository.get_by_id(ingredient.id)

        if existing is not None:
            raise DuplicateIngredientError(
                f"Ingredient with id {ingredient.id} already exists"
            )

        return self.repository.add(ingredient)

    def delete_ingredient(self, id: int) -> bool:
        deleted = self.repository.delete(id)

        if not deleted:
            raise IngredientNotFoundError(
                f"Ingredient with id {id} was not found"
            )

        return True

    def get_ingredient_by_id(self, id: int) -> Ingredient:
        ingredient = self.repository.get_by_id(id)

        if ingredient is None:
            raise IngredientNotFoundError(
                f"Ingredient with id {id} was not found"
            )

        return ingredient

    def get_ingredient_by_name(self, name: str) -> Ingredient:
        ingredient = self.repository.get_by_name(name)

        if ingredient is None:
            raise IngredientNotFoundError(
                f"Ingredient with name {name} was not found"
            )

        return ingredient

    def update_ingredient(self, id: int, ingredient: Ingredient) -> Ingredient:
        updated = self.repository.update(id, ingredient)

        if updated is None:
            raise IngredientNotFoundError(
                f"Ingredient with id {id} was not found"
            )

        return updated

    def get_ingredient_cost(self, id: int) -> float:
        cost = self.repository.get_cost(id)

        if cost is None:
            raise IngredientNotFoundError(
                f"Ingredient with id {id} was not found"
            )

        return cost

    def get_total_ingredient_cost(self) -> float:
        return self.repository.get_total_cost()
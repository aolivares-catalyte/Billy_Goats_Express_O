from models.ingredient import Ingredient
from repositories.ingredient_repository import IngredientRepository


def test_add():
    """Test that an ingredient can be added to the repository."""
    repo = IngredientRepository()
    repo.ingredients = []

    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")

    assert repo.add(ingredient) == ingredient


def test_delete_ingredient():
    """Test that an existing ingredient can be deleted from the repository."""
    repo = IngredientRepository()
    repo.ingredients = []

    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")
    repo.add(ingredient)

    assert repo.delete_ingredient(1) is True


def test_get_cost():
    """Test that an ingredient cost can be retrieved by ID."""
    repo = IngredientRepository()
    repo.ingredients = []

    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")
    repo.add(ingredient)

    assert repo.get_cost(1) == 5.0
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

def test_get_total_cost():
    """Test that the total cost of all ingredients is calculated correctly."""
    repo = IngredientRepository()
    repo.ingredients = []

    repo.add(Ingredient(1, "Sugar", 5.0, 1.0, "kg"))
    repo.add(Ingredient(2, "Salt", 3.0, 1.0, "kg"))

    assert repo.get_total_cost() == 8.0


def test_update():
    """Test that an existing ingredient can be updated."""
    repo = IngredientRepository()
    repo.ingredients = []

    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")
    repo.add(ingredient)

    updated = Ingredient(1, "Sugar", 6.0, 2.0, "kg")

    assert repo.update(1, updated) == updated


def test_get_by_id():
    """Test that an ingredient can be found by its ID."""
    repo = IngredientRepository()
    repo.ingredients = []

    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")
    repo.add(ingredient)

    assert repo.get_by_id(1) == ingredient


def test_get_by_name():
    """Test that an ingredient can be found by its name."""
    repo = IngredientRepository()
    repo.ingredients = []

    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")
    repo.add(ingredient)

    assert repo.get_by_name("Sugar") == ingredient
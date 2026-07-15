import pytest
from models.ingredient import Ingredient
from repositories.ingredient_repository import IngredientRepository
from services.ingredient_service import IngredientService
from exceptions import DuplicateIngredientError

@pytest.fixture
def repository():
    repo = IngredientRepository()
    repo.ingredients = []
    return repo

@pytest.fixture
def service(repository):
    return IngredientService(repository)

def test_add_ingredient(service):
    """Test that a new ingredient can be successfully added."""
    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")
    result = service.add_ingredient(ingredient)
    
    assert result == ingredient

def test_add_duplicate_ingredient(service):
    """Test that adding an ingredient with an existing ID raises an exception."""
    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")
    service.add_ingredient(ingredient)

    with pytest.raises(DuplicateIngredientError):
        service.add_ingredient(ingredient)

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
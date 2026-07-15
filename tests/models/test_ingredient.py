import pytest
from models.ingredient import Ingredient
from repositories.ingredient_repository import IngredientRepository
from services.ingredient_service import IngredientService
from exceptions import DuplicateIngredientError, IngredientNotFoundError

@pytest.fixture
def service(repository):
    return IngredientService(repository)

def test_add_ingredient(service):
    """Test that a new ingredient can be successfully added."""
    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")
    result = service.add_ingredient(ingredient)

    assert result == ingredient
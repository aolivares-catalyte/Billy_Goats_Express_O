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
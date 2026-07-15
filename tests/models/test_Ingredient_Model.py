from models.ingredient import Ingredient


def test_create_ingredient():
    """Test that an ingredient object is created with the correct attributes."""
    ingredient = Ingredient(1, "Sugar", 5.0, 1.0, "kg")

    assert ingredient.id == 1
    assert ingredient.name == "Sugar"
    assert ingredient.purchasing_cost == 5.0
    assert ingredient.unit_amount == 1.0
    assert ingredient.unit_of_measure == "kg"
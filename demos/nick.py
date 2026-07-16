from decimal import Decimal
from models.ingredient import Ingredient
from repositories.ingredient_repository import IngredientRepository
from services.ingredient_service import IngredientService
from exceptions import DuplicateIngredientError

def main():
    repository = IngredientRepository()
    service = IngredientService(repository)

    ingredient = Ingredient(
        id=1,
        name="Flour",
        purchasing_cost=Decimal("3.99"),
        unit_amount=5.0,
        unit_of_measure="lb"
    )

    service.add_ingredient(ingredient)
    print("An ingredient has been successfully added.")

    try:
        service.add_ingredient(ingredient)
    except DuplicateIngredientError as e:
        print(f"Error: This ingredient {e} has already been successfully added.")

if __name__ == "__main__":
    main()
from models.drink import Drink
from repositories.drink_repository import DrinkRepository
from exceptions import DuplicateDrinkError

class DrinkService:
    """A service for managing Drinks"""

    def __init__(self, repository: DrinkRepository) -> None:
        """Create a new drink service.

        Args:
            repository: The repository containing the drinks.
        
        Raises:
            DuplicateDrinkError: If any two drinks have the same ID.
            DuplicateEmailError: If any two drinks have the same email.
            InvalidEmailError: If any drink has an invalid (malformed) email.
        """
        self._repository = repository

    def get_all_drinks(self) -> list[Drink]:
        """Get all drinks in the service.

        Returns:
            A list containing the drinks.
        """
        return []

    def get_drink_by_id(self, id: int) -> Drink | None:
        """Search for a drink by ID.

        Args:
            id: The drink ID.

        Returns:
            The drink with the provided ID, or None if not found.
        """
        self._repository.get_by_id(id)

    def get_drink_by_name(self, name: str) -> Drink | None:
        """Search for a drink by name.

        Args:
            name: The drink name.

        Returns:
            The drink with the provided name, or None if not found.
        """
        self._repository.get_by_name(name)

    def create_drink(self, drink: Drink) -> Drink:
        """Add a new drink to the service.

        Args:
            drink: The drink to add.

        Raises:
            DuplicateDrinkError: If the drink has the same ID as one already managed by the service.
            DuplicateEmailError: If the drink has the same email as one already managed by the service.
            InvalidEmailError: If the drink has an invalid (malformed) email.

        Returns:
            The drink that was added.
        """
        if self._repository.get_by_name(drink.name) is not None:
            msg = f"Drink {drink.name} already exists"
            raise DuplicateDrinkError(msg)
        elif self._repository.get_by_id(drink.id) is not None:
            msg = f"Drink {drink.id} already exists"
            raise DuplicateDrinkError(msg)
        else:
            # calculate the sale_price
            drink.sale_price = drink.cost_to_produce * drink.markup_percentage
            return self._repository.add(drink)

    def update_drink(self, id: int, drink: Drink) -> Drink | None:
        """Add a new drink to the service.

        Args:
            drink: The drink to add.

        Raises:
            DuplicateDrinkError: If the drink has the same ID as one already managed by the service.
            DuplicateEmailError: If the drink has the same email as one already managed by the service.
            InvalidEmailError: If the drink has an invalid (malformed) email.

        Returns:
            The drink that was added.
        """
        return self._repository.update(id, drink)

    def delete_drink(self, id: int) -> bool:
        """Remove a drink from the service.

        Args:
            drink: The ID of the drink to remove.

        Returns:
            True if found and removed, False otherwise.
        """
        return self._repository.delete(id)

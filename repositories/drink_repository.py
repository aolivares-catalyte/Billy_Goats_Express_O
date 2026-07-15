from models.drink import Drink

class DrinkRepository:
    """Manages the list of Drinks."""

    def __init__(self):
        self._drinks: list[Drink] = []

    def get_all(self) -> list[Drink]:
        """Return a list containing all Drinks in the repository."""
        return self._drinks

    def get_by_id(self, id: int) -> Drink | None:
        """Search the repository for a Drink with the provided id.

        Args:
            id: The Drink ID to search for.

        Returns:
            The Drink with the specified ID, or None if not found.
        """
        return next((d for d in self._drinks if d.id == id), None)

    def get_by_name(self, name: str) -> Drink | None:
        """Search the repository for a Drink with the provided name.

        Args:
            name: The Drink name to search for.

        Returns:
            The Drink with the specified name, or None if not found.
        """
        return next((d for d in self._drinks if d.name == name), None)

    def add(self, drink: Drink) -> Drink:
        """Add a Drink to the repository.

        Args:
            drink: The Drink to add.

        Returns:
            The Drink that was added.
        """
        self._drinks.append(drink)
        return drink

    def update(self, id: int, drink: Drink) -> Drink | None:
        """Replace the Drink with the specified ID.

        Args:
            id: The ID of the Drink to be removed.
            drink: The Drink to add in its place.

        Returns:
            The Drink that was added, or None if no Drink with the provided ID
            was found.
        """
        drink_index = next((i for (i, c) in enumerate(self._drinks) if c.id == id), None)
        if drink_index is not None:
            self._drinks[drink_index] = drink
            return drink
        else:
            return None

    def delete(self, id: int) -> bool:
        """Remove the Drink with the specified ID.

        Args:
            id: The ID of the Drink to be removed.

        Returns:
            True if the Drink was found and removed, False if not found.
        """
        drink_index = next((i for (i, c) in enumerate(self._drinks) if c.id == id), None)
        if drink_index is not None:
            self._drinks.pop(drink_index)
            return True
        else:
            return False

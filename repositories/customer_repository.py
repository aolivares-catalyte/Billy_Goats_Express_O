from models.customer import Customer

class CustomerRepository:
    """Manages the list of Customers."""

    def __init__(self):
        self._customers: list[Customer] = []

    def get_all(self) -> list[Customer]:
        """Return a list containing all Customers in the repository."""
        return self._customers

    def get_by_id(self, id: int) -> Customer | None:
        """Search the repository for a Customer with the provided id.

        Args:
            id: The Customer ID to search for.

        Returns:
            The Customer with the specified ID, or None if not found.
        """
        return next((c for c in self._customers if c.id == id), None)

    def get_by_name(self, name: str) -> Customer | None:
        """Search the repository for a Customer with the provided name.

        Args:
            name: The Customer name to search for.

        Returns:
            The Customer with the specified name, or None if not found.
        """
        return next((c for c in self._customers if c.name == name), None)

    def add(self, customer: Customer) -> Customer:
        """Add a Customer to the repository.

        Args:
            customer: The Customer to add.

        Returns:
            The Customer that was added.
        """
        self._customers.append(customer)
        return customer

    def update(self, id: int, customer: Customer) -> Customer | None:
        """Replace the Customer with the specified ID.

        Args:
            id: The ID of the Customer to be removed.
            customer: The Customer to add in its place.

        Returns:
            The Customer that was added, or None if no Customer with the provided ID
            was found.
        """
        customer_index = next((i for (i, c) in enumerate(self._customers) if c.id == id), None)
        if customer_index is not None:
            self._customers[customer_index] = customer
            return customer
        else:
            return None

    def delete(self, id: int) -> bool:
        """Remove the Customer with the specified ID.

        Args:
            id: The ID of the Customer to be removed.

        Returns:
            True if the Customer was found and removed, False if not found.
        """
        customer_index = next((i for (i, c) in enumerate(self._customers) if c.id == id), None)
        if customer_index is not None:
            self._customers.pop(customer_index)
            return True
        else:
            return False

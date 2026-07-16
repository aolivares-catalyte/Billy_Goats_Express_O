import re
from exceptions import DuplicateCustomerError, InvalidEmailError, DuplicateEmailError
from models.customer import Customer
from repositories.customer_repository import CustomerRepository

def validate_email(email: str, customer_repository: CustomerRepository):
    split_at = email.split("@")
    if len(split_at) != 2:
        raise InvalidEmailError("Email {email} must contain one '@' character")
    else:
        username, server = split_at

    split_dot = server.split(".")
    if len(split_dot) != 2:
        raise InvalidEmailError("Server {server} must contain one '.' character")
    else:
        domain, extension = split_dot

    if not re.match("[A-Za-z0-9]", username):
        raise InvalidEmailError("Username #{username} contains invalid characters")
    elif len(username) < 1:
        raise InvalidEmailError("Username #{username} must be at least one character")
    elif len(username) > 30:
        raise InvalidEmailError("Username #{username} must be less than 30 characters")
    elif not re.match("[A-Za-z0-9]", domain):
        raise InvalidEmailError("Domain #{domain} contains invalid characters")
    elif len(domain) < 1:
        raise InvalidEmailError("Domain #{domain} must be at least one character")
    elif len(domain) > 30:
        raise InvalidEmailError("Domain #{domain} must be less than 30 characters")
    elif not re.match("[A-Za-z0-9]", extension):
        raise InvalidEmailError("Extension #{extension} contains invalid characters")
    elif len(extension) < 2:
        raise InvalidEmailError("Extension #{extension} must be at least two characters")
    elif len(extension) > 15:
        raise InvalidEmailError("Extension #{extension} must be less than 15 characters")
    elif email in map(lambda c: c.email, customer_repository.get_all()):
        raise DuplicateEmailError("Email #{email} must be unique")

def validate_id(id: int, customer_repository: CustomerRepository, allow_one: bool = False):
    existing = customer_repository.get_by_id(id)
    pool = customer_repository.get_all()
    if customer_repository.get_by_id(id) is not None:
        if allow_one:
            count = len(filter(lambda c: c.id == id, customer_repository.get_all()))
            if not count <= 1:
                raise DuplicateCustomerError("Customer {customer.id} already exists")

def validate_name(name: str, customer_repository: CustomerRepository):
    if customer_repository.get_by_name(name) is not None:
        raise DuplicateCustomerError("Customer {customer.name} already exists")

class CustomerService:
    """A service for managing Customers"""

    def __init__(self, repository: CustomerRepository) -> None:
        """Create a new customer service.

        Args:
            repository: The repository containing the customers.
        
        Raises:
            DuplicateCustomerError: If any two customers have the same ID.
            DuplicateEmailError: If any two customers have the same email.
            InvalidEmailError: If any customer has an invalid (malformed) email.
        """
        self._repository = repository

    def get_all_customers(self) -> list[Customer]:
        """Get all customers in the service.

        Returns:
            A list containing the customers.
        """
        return self._repository.get_all()

    def get_customer_by_id(self, id: int) -> Customer | None:
        """Search for a customer by ID.

        Args:
            id: The customer ID.

        Returns:
            The customer with the provided ID, or None if not found.
        """
        self._repository.get_by_id(id)

    def get_customer_by_name(self, name: str) -> Customer | None:
        """Search for a customer by name.

        Args:
            name: The customer name.

        Returns:
            The customer with the provided name, or None if not found.
        """
        self._repository.get_by_name(name)

    def create_customer(self, customer: Customer) -> Customer:
        """Add a new customer to the service.

        Args:
            customer: The customer to add.

        Raises:
            DuplicateCustomerError: If the customer has the same ID as one already managed by the service.
            DuplicateEmailError: If the customer has the same email as one already managed by the service.
            InvalidEmailError: If the customer has an invalid (malformed) email.

        Returns:
            The customer that was added.
        """
        validate_id(customer.id, self._repository)
        validate_email(customer.email, self._repository)
        validate_name(customer.name, self._repository)
        return self._repository.add(customer)

    def update_customer(self, id: int, customer: Customer) -> Customer | None:
        """Add a new customer to the service.

        Args:
            customer: The customer to add.

        Raises:
            DuplicateCustomerError: If the customer has the same ID as one already managed by the service.
            DuplicateEmailError: If the customer has the same email as one already managed by the service.
            InvalidEmailError: If the customer has an invalid (malformed) email.

        Returns:
            The customer that was added.
        """
        validate_email(customer.email, self._repository)
        validate_name(customer.name, self._repository)
        return self._repository.update(id, customer)

    def delete_customer(self, id: int) -> bool:
        """Remove a customer from the service.

        Args:
            customer: The ID of the customer to remove.

        Returns:
            True if found and removed, False otherwise.
        """
        return self._repository.delete(id)

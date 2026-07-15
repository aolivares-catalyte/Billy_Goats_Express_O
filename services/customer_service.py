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

class CustomerService:
    def __init__(self, repository: CustomerRepository) -> None:
        self._repository = repository

    def create_customer(self, customer: Customer) -> Customer:
        if self._repository.get_by_name(customer.name) is not None:
            msg = f"Customer {customer.name} already exists"
            raise DuplicateCustomerError(msg)
        elif self._repository.get_by_id(customer.id) is not None:
            msg = f"Customer {customer.id} already exists"
            raise DuplicateCustomerError(msg)
        else:
            validate_email(customer.email, self._repository)
            return self._repository.add(customer)

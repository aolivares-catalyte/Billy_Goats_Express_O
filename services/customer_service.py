from models.customer import Customer
from repositories.customer_repository import CustomerRepository
from exceptions import DuplicateCustomerError

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
            return self._repository.add(customer)

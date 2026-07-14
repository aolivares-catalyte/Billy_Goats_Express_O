import pytest
from exceptions import DuplicateCustomerError
from models.drink import Drink, Ingredient
from models.customer import Customer
from repositories.drink_repository import DrinkRepository
from services.drink_service import DrinkService
from decimal import Decimal

def test_duplicate_customer_name_should_raise_DuplicateCustomerError(sample_customer_service):
    with pytest.raises(DuplicateCustomerError):
        customer = Customer(3, "Priya Chandrasekaran", "priya@example.com", Decimal("0.0"))
        sample_customer_service.create_customer(customer)

def test_duplicate_customer_id_should_raise_DuplicateCustomerError(sample_customer_service):
    with pytest.raises(DuplicateCustomerError):
        customer = Customer(1, "Anna Flores", "anna.flores@example.com", Decimal("1700.77"))
        sample_customer_service.create_customer(customer)

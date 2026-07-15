import pytest
from decimal import Decimal
from exceptions import DuplicateCustomerError, InvalidEmailError, DuplicateEmailError
from models.customer import Customer
from repositories.customer_repository import CustomerRepository
from services.customer_service import validate_email

def test_duplicate_customer_name_should_raise_DuplicateCustomerError(sample_customer_service):
    with pytest.raises(DuplicateCustomerError):
        customer = Customer(3, "Priya Chandrasekaran", "priya@example.com", Decimal("0.0"))
        sample_customer_service.create_customer(customer)

def test_duplicate_customer_id_should_raise_DuplicateCustomerError(sample_customer_service):
    with pytest.raises(DuplicateCustomerError):
        customer = Customer(1, "Anna Flores", "anna.flores@example.com", Decimal("1700.77"))
        sample_customer_service.create_customer(customer)

@pytest.mark.parametrize("email", [
   "@example.com",
   "test@.com",
   "test@example.",
   "test@examplecom",
   "example.com",
   "this-is-an-example-username-string@example.com",
   "test@this-is-an-example-server-name-string.com",
   "test@example.x",
   "test@example.this-is-an-example-tld",
])
def test_should_reject_invalid_email_address(email):
    with pytest.raises(InvalidEmailError):
        validate_email(email, CustomerRepository())

def test_should_reject_duplicate_email_address(priya, sample_customer_repository):
    with pytest.raises(DuplicateEmailError):
        validate_email(priya.email, sample_customer_repository)

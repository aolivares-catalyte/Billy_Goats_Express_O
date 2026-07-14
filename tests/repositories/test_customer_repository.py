import pytest
from repositories.customer_repository import CustomerRepository

def test_new_customer_repository_should_have_no_customers():
    repo = CustomerRepository()
    assert len(repo.get_all()) == 0

def test_add_should_add(marcus):
    repo = CustomerRepository()
    before_count = len(repo.get_all())
    repo.add(marcus)
    after_count = len(repo.get_all())
    assert after_count == before_count + 1

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

def test_get_by_id_should_return_requested_customer(sample_customer_repository, marcus):
    assert sample_customer_repository.get_by_id(marcus.id) == marcus

def test_get_by_name_should_return_requested_customer(sample_customer_repository, priya):
    assert sample_customer_repository.get_by_name(priya.name) == priya

def test_update_should_replace_customer(sample_customer_repository, priya, diego):
    sample_customer_repository.update(priya.id, diego)
    assert sample_customer_repository.get_by_id(priya.id) is None
    assert sample_customer_repository.get_by_id(diego.id) == diego

def test_delete_should_delete_customer(sample_customer_repository, marcus):
    before_count = len(sample_customer_repository.get_all())
    was_deleted = sample_customer_repository.delete(marcus.id)
    after_count = len(sample_customer_repository.get_all())
    assert was_deleted
    assert after_count == before_count - 1
    assert sample_customer_repository.get_by_id(marcus.id) is None

def test_delete_should_return_false_if_customer_not_found(sample_customer_repository, diego):
    before_count = len(sample_customer_repository.get_all())
    was_deleted = sample_customer_repository.delete(diego.id)
    after_count = len(sample_customer_repository.get_all())
    assert not was_deleted
    assert after_count == before_count

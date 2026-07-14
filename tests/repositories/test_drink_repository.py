import pytest
from repositories.drink_repository import DrinkRepository

def test_new_drink_repository_should_have_no_drinks():
    repo = DrinkRepository()
    assert len(repo.get_all()) == 0

def test_add_should_add(black_tea):
    repo = DrinkRepository()
    before_count = len(repo.get_all())
    repo.add(black_tea)
    after_count = len(repo.get_all())
    assert after_count == before_count + 1

def test_get_by_id_should_return_requested_drink(sample_drink_repository, americano):
    assert sample_drink_repository.get_by_id(americano.id) == americano

def test_get_by_name_should_return_requested_drink(sample_drink_repository, latte):
    assert sample_drink_repository.get_by_name(latte.name) == latte

def test_update_should_replace_drink(sample_drink_repository, americano, black_tea):
    sample_drink_repository.update(americano.id, black_tea)
    assert sample_drink_repository.get_by_id(americano.id) is None
    assert sample_drink_repository.get_by_id(black_tea.id) == black_tea

def test_delete_should_delete_drink(sample_drink_repository, americano):
    before_count = len(sample_drink_repository.get_all())
    was_deleted = sample_drink_repository.delete(americano.id)
    after_count = len(sample_drink_repository.get_all())
    assert was_deleted
    assert after_count == before_count - 1
    assert sample_drink_repository.get_by_id(americano.id) is None

def test_delete_should_return_false_if_drink_not_found(sample_drink_repository, black_tea):
    before_count = len(sample_drink_repository.get_all())
    was_deleted = sample_drink_repository.delete(black_tea.id)
    after_count = len(sample_drink_repository.get_all())
    assert not was_deleted
    assert after_count == before_count

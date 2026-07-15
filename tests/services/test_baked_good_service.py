from decimal import Decimal

import pytest

from exceptions import (
    BakedGoodNotFoundError,
    DuplicateBakedGoodError,
)
from models.baked_good import BakedGood
from repositories.baked_good_repository import BakedGoodRepository
from services.baked_good_service import BakedGoodService


class TestBakedGoodService:
    """Test suite for the BakedGoodService class."""

    def setup_method(self):
        """Creates a fresh repository and service before each test."""

        self.repository = BakedGoodRepository()
        self.service = BakedGoodService(self.repository)

        self.baked_good = BakedGood(
            id=1,
            name="Blueberry Muffin",
            purchasing_cost=Decimal("2.00"),
            markup_percentage=Decimal("50"),
            vendor_name="Sweet Bakery",
            allergens=["Wheat", "Milk", "Eggs"],
        )

    def test_create_baked_good(self):
        """Verifies that a baked good is successfully created."""

        result = self.service.create_baked_good(self.baked_good)

        assert result == self.baked_good

    def test_duplicate_baked_good_raises_exception(self):
        """Verifies that duplicate baked goods are not allowed."""

        self.service.create_baked_good(self.baked_good)

        with pytest.raises(DuplicateBakedGoodError):
            self.service.create_baked_good(self.baked_good)

    def test_get_existing_baked_good(self):
        """Verifies that an existing baked good can be retrieved."""

        self.service.create_baked_good(self.baked_good)

        result = self.service.get_baked_good(self.baked_good.name)

        assert result == self.baked_good

    def test_get_nonexistent_baked_good_returns_none(self):
        """Verifies that a nonexistent baked good returns None."""

        result = self.service.get_baked_good("Chocolate Croissant")

        assert result is None

    def test_update_nonexistent_baked_good_raises_exception(self):
        """Verifies that updating a nonexistent baked good raises an exception."""

        updated_baked_good = BakedGood(
            id=2,
            name="Chocolate Croissant",
            purchasing_cost=Decimal("3.00"),
            markup_percentage=Decimal("50"),
            vendor_name="Bakery",
            allergens=["Wheat"],
        )

        with pytest.raises(BakedGoodNotFoundError):
            self.service.update_baked_good(
                "Chocolate Croissant",
                updated_baked_good,
            )

    def test_delete_nonexistent_baked_good_raises_exception(self):
        """Verifies that deleting a nonexistent baked good raises an exception."""

        with pytest.raises(BakedGoodNotFoundError):
            self.service.delete_baked_good("Chocolate Croissant")
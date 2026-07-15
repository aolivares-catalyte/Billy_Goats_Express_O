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

    def setup_method(self) -> None:
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
        assert len(self.service.get_all_baked_goods()) == 1

    def test_duplicate_baked_good_raises_exception(self):
        """Verifies that creating a baked good with an existing name raises DuplicateBakedGoodError."""

    # Arrange
        self.service.create_baked_good(self.baked_good)

    # Act & Assert
        with pytest.raises(DuplicateBakedGoodError):
            self.service.create_baked_good(self.baked_good)

    def test_get_existing_baked_good(self):
        """Verifies that an existing baked good can be retrieved by name."""

        # Arrange
        self.service.create_baked_good(self.baked_good)

        # Act
        result = self.service.get_baked_good(self.baked_good.name)

        # Assert
        assert result is not None
        assert result == self.baked_good

    def test_get_nonexistent_baked_good_returns_none(self):
        """Verifies that requesting a baked good that does not exist returns None."""

        result = self.service.get_baked_good("Chocolate Croissant")

        assert result is None

    def test_get_all_baked_goods(self):
        """Verifies that all baked goods are returned."""

        self.service.create_baked_good(self.baked_good)

        baked_goods = self.service.get_all_baked_goods()

        assert len(baked_goods) == 1
        assert baked_goods[0].name == "Blueberry Muffin"

    
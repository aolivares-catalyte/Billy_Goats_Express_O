from decimal import Decimal

import pytest

from models.baked_good import BakedGood
from repositories.baked_good_repository import BakedGoodRepository
from services.baked_good_service import BakedGoodService
from exceptions import (
    DuplicateBakedGoodError,
    BakedGoodNotFoundError,
)


class TestBakedGoodService:
    
    """Test suite for the BakedGoodService class."""
    

    def setup_method(self):
        
        """Creates a fresh repository and service before each test."""
        self.repository = BakedGoodRepository()
        self.service = BakedGoodService(self.repository)

        self.baked_good = BakedGood(
            name="Blueberry Muffin",
            purchasing_cost=Decimal("2.00"),
            markup_percentage=Decimal("50"),
            vendor_name="Sweet Bakery",
            allergens=["Wheat", "Milk", "Eggs"]
        )

    def test_create_baked_good(self):
        """
        Verifies that a baked good is successfully created.
        """
        result = self.service.create_baked_good(self.baked_good)

        assert result == self.baked_good
        assert len(self.service.get_all_baked_goods()) == 1

    def test_duplicate_baked_good_raises_exception(self):
        """
        Verifies that creating a duplicate baked good raises
        DuplicateBakedGoodError.
        """
        self.service.create_baked_good(self.baked_good)

        with pytest.raises(DuplicateBakedGoodError):
            self.service.create_baked_good(self.baked_good)


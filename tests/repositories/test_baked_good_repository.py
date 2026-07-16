from decimal import Decimal

from models.baked_good import BakedGood
from repositories.baked_good_repository import BakedGoodRepository


class TestBakedGoodRepository:
    """Test suite for the BakedGoodRepository class."""

    def setup_method(self):
        """Creates a fresh repository before each test."""

        self.repository = BakedGoodRepository()

        self.baked_good = BakedGood(
            id=1,
            name="Blueberry Muffin",
            purchasing_cost=Decimal("2.00"),
            markup_percentage=Decimal("50"),
            vendor_name="Sweet Bakery",
            allergens=["Wheat", "Milk", "Eggs"],
        )

    def test_add_baked_good(self):
        """Verifies a baked good can be added."""

        result = self.repository.add(self.baked_good)

        assert result == self.baked_good
        assert len(self.repository.get_all()) == 1

    def test_get_all_returns_all_baked_goods(self):
        """Verifies all baked goods are returned."""

        self.repository.add(self.baked_good)

        baked_goods = self.repository.get_all()

        assert len(baked_goods) == 1
        assert baked_goods[0] == self.baked_good

    def test_get_by_name_returns_baked_good(self):
        """Verifies a baked good can be retrieved by name."""

        self.repository.add(self.baked_good)

        result = self.repository.get_by_name(
            self.baked_good.name
        )

        assert result == self.baked_good

    def test_get_by_name_returns_none_when_not_found(self):
        """Verifies None is returned when a baked good is not found."""

        result = self.repository.get_by_name(
            "Chocolate Croissant"
        )

        assert result is None

    def test_delete_existing_baked_good(self):
        """Verifies an existing baked good can be deleted."""

        self.repository.add(self.baked_good)

        result = self.repository.delete(
            self.baked_good.name
        )

        assert result is True
        assert len(self.repository.get_all()) == 0

    def test_delete_nonexistent_baked_good(self):
        """Verifies False is returned when deleting a nonexistent baked good."""

        result = self.repository.delete(
            "Chocolate Croissant"
        )

        assert result is False
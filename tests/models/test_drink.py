import pytest
from decimal import Decimal, localcontext
from models.drink import Drink

@pytest.mark.parametrize("input, expected", [
    ([1, "Americano", [], Decimal("5.60"), Decimal("0.30")], Decimal("7.28")),
    ([2, "Vanilla Latte", [], Decimal("7.60"), Decimal("0.25")], Decimal("9.50")),
])
def test_sale_price_should_be_calculated_from_cost_to_produce_and_markup_percentage(input, expected):
    drink = Drink(*input)
    assert drink.sale_price == expected

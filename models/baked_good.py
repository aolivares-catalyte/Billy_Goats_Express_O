from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


@dataclass
class BakedGood:
    id: int
    name: str
    purchasing_cost: Decimal
    markup_percentage: Decimal
    vendor_name: str
    allergens: list[str]
    sale_price: Decimal = field(init=False)

    def __post_init__(self) -> None:
        print(
        "DEBUG:",
        self.purchasing_cost,
        self.markup_percentage
    )
        markup_amount = (
            self.purchasing_cost * self.markup_percentage
        ) / Decimal("100")

        self.sale_price = (
            self.purchasing_cost + markup_amount
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Customer:
    id: int
    name: str
    email: str
    lifetime_spent: Decimal

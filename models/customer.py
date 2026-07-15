from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Customer:
    """Represents an Expresso-O customer.

    This is a plain data container. Invariants are enforced by CustomerService.

    Attributes:
        id: A unique integer ID.
        name: The customer's full name ("Susan Smith").
        email: The customer's email.
        lifetime_spent: The amount of money the customer has spent since their
            registration.
    """
    id: int
    name: str
    email: str
    lifetime_spent: Decimal = Decimal("0.0")

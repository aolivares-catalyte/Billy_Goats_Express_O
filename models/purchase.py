from dataclasses import dataclass
from datetime import datetime, timezone
from customer import Customer
from decimal import Decimal
@dataclass
class Purchase:
    timestamp:datetime = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    items:list
    total_cost:Decimal
    customer:Customer

from dataclasses import dataclass,field
from datetime import datetime, timezone
from customer import Customer
from decimal import Decimal
@dataclass
class Purchase:
    id:int
    timestamp:datetime = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    items:list
    total_cost:Decimal = field(init=False)
    customer:Customer
    def __post_init__(self):
        self.total_cost = sum(i.sale_price for i in self.items)

        

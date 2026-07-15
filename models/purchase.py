from dataclasses import dataclass,field
from datetime import datetime, timezone
from models.customer import Customer
from decimal import Decimal

@dataclass
class Purchase:
    id:int
    items:list
    customer:Customer

    timestamp:datetime = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    total_cost:Decimal = field(init=False)
    
    
    def __post_init__(self):
        self.items = []
        self.total_cost = sum(i.sale_price for i in self.items)


        

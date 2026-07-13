from dataclasses import dataclass
import datetime
from customer import Customer
@dataclass
class Purchase:
    timestamp:datetime
    items:list
    total_cost:float
    customer:Customer

import pytest
from models.purchase import Purchase
from models.baked_good import BakedGood
from models.drink import Drink
from models.customer import Customer
from models.ingredient import Ingredient
from repositories.purchase_repository import PurchaseRepository
from decimal import Decimal
from datetime import datetime, timezone

d=Drink(0,"Matcha",[Ingredient(90,"grass",12.99,10.00,"LBS")],90.99,10.00)
b=BakedGood(11,"cookie",10.00,1.99,"Starbucks","Peanuts")
a1=Purchase(12,datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),[d,b],120.00,Customer(99,"Allen","aolivares1042@gmail.com",2000.00))

print(a1)
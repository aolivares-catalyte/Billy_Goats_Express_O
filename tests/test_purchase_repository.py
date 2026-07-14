from models.purchase import Purchase
from models.baked_good import BakedGood
from models.drink import Drink
from models.ingredient import Ingredient
from repositories.purchase_repository import PurchaseRepository
import pytest
from decimal import Decimal
from datetime import datetime, timezone

d=Drink(0,"Matcha",[Ingredient(90,"grass",12.99,10.00,"LBS")],90.99,10.00)
b=BakedGood(11,"cookie",10.00,1.99,"sta")

Purchase(12,datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),)
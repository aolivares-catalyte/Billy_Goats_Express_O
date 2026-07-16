from services.baked_good_service import BakedGoodService
from repositories.baked_good_repository import BakedGoodRepository
from models.baked_good import BakedGood
from decimal import Decimal

# baked_good = BakedGoodService(BakedGoodRepository())
# bill = Customer(1, "Bill Walters", "bill.walters@example.com", Decimal("560.78"))
# baked_good.create_baked_good(bill)

repository = BakedGoodRepository()
service = BakedGoodService(repository)

danish = BakedGood(
    id=333,
    name="Danish",
    purchasing_cost=Decimal("2.00"),
    markup_percentage=Decimal("50"),
    vendor_name="Sweet Bakery",
    allergens=["Wheat", "Milk", "Eggs"]
)
service.create_baked_good(danish)

baked_goods = service.get_all_baked_goods()

print("Current Baked Goods:")

for baked_good in baked_goods:
    print(baked_good)

print(service.get_all_baked_goods())

apple_pie = BakedGood(
    id=555,
    name="Apple Pie",
    purchasing_cost=Decimal("2.00"),
    markup_percentage=Decimal("50"),
    vendor_name="WsG Farms",
    allergens=["Milk", "Eggs"]
)
service.create_baked_good(apple_pie)

strawberry_muffin = BakedGood(
    id=999,
    name="Strawberry Muffin",
    purchasing_cost=Decimal("1.25"),
    markup_percentage=Decimal("70"),
    vendor_name="Sweet Bakery",
    allergens=["Wheat", "Milk", "Eggs"]
)
service.create_baked_good(strawberry_muffin)

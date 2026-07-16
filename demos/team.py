from services.purchase_service import PurchaseService
from repositories.purchase_repository import PurchaseRepository
from models.purchase import Purchase
from decimal import Decimal
from models.customer import Customer
from services.customer_service import CustomerService
from repositories.customer_repository import CustomerRepository
from services.purchase_service import PurchaseService
from repositories.purchase_repository import PurchaseRepository
from models.customer import Customer
from decimal import Decimal
from models.drink import Drink
from models.ingredient import Ingredient
from datetime import datetime, timezone
from repositories.ingredient_repository import IngredientRepository
from services.ingredient_service import IngredientService
from exceptions import DuplicateIngredientError
from services.baked_good_service import BakedGoodService
from repositories.baked_good_repository import BakedGoodRepository
from models.baked_good import BakedGood
from decimal import Decimal

# Preassembled Services / Objects

purchase_service = PurchaseService(PurchaseRepository())
d= datetime(2020, 1, 1, tzinfo=timezone.utc)
beans=Ingredient(1, "Coffee Beans", Decimal("2.50"), 14.0, "g")
water=Ingredient(2, "Water", Decimal("0.01"), 250.0, "g")
milk=Ingredient(3, "Milk", Decimal("1.25"), 250.0, "g")
latte=Drink(2, "Latte", [beans, water, milk], Decimal("5.00"),Decimal("1.25") )
blueberry_muffin=Ingredient(2, "Water", Decimal("0.01"), 250.0, "g")
alex=Customer(99,"Alex","aolivares1042@gmail.com",Decimal("2000.00"))
# alex_purchase = Purchase(120,[blueberry_muffin,latte],alex,d)
# purchase_service.create_purchase(alex_purchase)

customer_service = CustomerService(CustomerRepository())
bill = Customer(1, "Bill Walters", "bill.walters@example.com", Decimal("560.78"))
customer_service.create_customer(bill)

# Shared Input/Ouput Routines

def prompt(prompt: str, options: list[tuple[int, str]]) -> int:
    while True:
        print(prompt)
        for option_id, option_text in options:
            print(f"{option_id}) {option_text}")
        print("=> ", end="", flush=True)

        try:
            choice = int(input())
        except ValueError:
            choice = None

        if choice in list(map(lambda o: o[0], options)):
            return choice
        else:
            print("Please enter a valid option.")

def fresh_id(list: list) -> int:
    all_ids = map(lambda o: o.id, list)
    return max(all_ids) + 1

# Customers

def show_customers():
    customers = customer_service.get_all_customers()
    print(f"=== DISPLAYING CUSTOMERS (Total: {len(customers):02}) ===")
    for customer in customers:
        print(f"Customer ID: {customer.id}")
        print(f"    Name: {customer.name}")
        print(f"    Email: {customer.email}")
        print(f"    Lifetime Spent: ${customer.lifetime_spent}")
        print()
    print(f"=== END CUSTOMERS ======================")
    print()

def add_customer():
    print("Add Customer:")
    print("Customer Name => ", end="", flush=True)
    name = input()
    print("Customer Email => ", end="", flush=True)
    email = input()
    id = fresh_id(customer_service.get_all_customers())
    customer_service.create_customer(Customer(id, name, email))

# Ingredients

def add_ingredient():
    repository = IngredientRepository()
    service = IngredientService(repository)

    ingredient = Ingredient(
        id=1,
        name="Flour",
        purchasing_cost=Decimal("3.99"),
        unit_amount=5.0,
        unit_of_measure="lb"
    )

    service.add_ingredient(ingredient)
    print("An ingredient has been successfully added.")

    try:
        service.add_ingredient(ingredient)
    except DuplicateIngredientError as e:
        print(f"Error: This ingredient {e} has already been successfully added.")

# Baked Goods

def add_baked_good():
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

# Menus

def baked_goods_menu() -> bool:
    print("")
    choice = prompt("Please select an option:", [
        (1, "Show All Baked Goods"),
        (2, "Search Baked Goods"),
        (3, "Delete Baked Good"),
        (4, "Return to Main Menu")
    ])

    if choice == 1:
        # show_all_baked_goods()
        return True
    elif choice == 2:
        # search_baked_goods()
        return True
    elif choice == 3:
        # delete_baked_good()
        return True
    else:
        return False

def main_menu() -> bool:
    print("Welcome to Express-O Point-of-Sale!")
    choice = prompt("Please select an option:", [
        (1, "Show All Customers"),
        (2, "Add Customer"),
        (4, "Manage Baked Goods"),
        (3, "Exit")
    ])

    if choice == 1:
        show_customers()
        return True
    elif choice == 2:
        add_customer()
        return True
    elif choice == 4:
        while baked_goods_menu():
            pass
        return True
    else:
        return False

def main():
    while main_menu():
        pass

if __name__ == "__main__":
    main()

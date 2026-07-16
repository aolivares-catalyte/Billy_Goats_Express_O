# Run this application with "python -m demos.team"
from exceptions import DuplicateIngredientError, IncorrectDateFormat
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
from exceptions import DuplicateIngredientError, InvalidEmailError, DuplicateEmailError, DuplicateCustomerError
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

    try:
        customer_service.create_customer(Customer(id, name, email))
        print("Customer added successfully!")
    except InvalidEmailError as e:
        print(f"ERROR: Invalid email: {str(e)}")
        print("Please re-enter customer details.")
    except DuplicateEmailError as e:
        print(f"ERROR: Invalid email: {str(e)}")
        print("Please re-enter customer details.")
    except DuplicateCustomerError as e:
        print(f"ERROR: Duplicate customer: {str(e)}")
        print("Please re-enter customer details.")

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


#Purchase

def show_all_purchases():
    purchases = purchase_service.get_all_purchases()
    print(f"Showing all of the purchases made (Total: {len(purchases)})")
    for purchase in purchases:
        print(f"Purchase ID: {purchase.id}")
        print(f"    Timestamp: {purchase.timestamp}")
        print(f"    Customer: {purchase.customer.name}")
        print(f"    Total Cost: ${purchase.total_cost}")
        
        item_names = [item.name for item in purchase.items]
        formatted_items = ", ".join(item_names)
        print(f"    Items: {formatted_items}\n")
        
    print(f"----All Purchases---\n")
    
def get_purchases_by_date():
    print("Search Purchases by Date:")
    print("Date (YYYY-MM-DD) => ", end="", flush=True) 
    date_str = input()
    
    try:
        purchases = purchase_service.get_all_purchases_by_date(date_str)
        print(f"\nPurchases matching date (Total: {len(purchases)}) \n")
        for purchase in purchases:
            print(f"Purchase ID: {purchase.id}")
            print(f"    Customer: {purchase.customer.name}")
            print(f"    Total Cost: ${purchase.total_cost}")
            print()
        print(f"End of purchases \n")
    except IncorrectDateFormat as e:
        print(f"\nERROR {e}\n")

def get_most_frequent_purchase():
    print("The MOST FREQUENTLY PURCHASED item is: \n")
    popular_item = purchase_service.get_most_frequent_item()
    
    if popular_item:
        print(f"The current fan-favorite is: {popular_item}")
    else:
        print("No purchases found in the system yet.")
    print("-----------------------\n")

# Menus

def ingredients_menu() -> bool:
    print()
    print(">>> Ingredients Menu <<<")
    print("------------------------")
    choice = prompt("Please select an option:", [
        (1, "Add New Ingredient ➕"),
        (2, "Return to Main Menu ⬅️"),
    ])

    if choice == 1:
        # add_ingredient()
        return True
    else:
        return False

def baked_goods_menu() -> bool:
    print()
    print(">>> Baked Goods Menu <<<")
    print("------------------------")
    choice = prompt("Please select an option:", [
        (1, "Show All Baked Goods 🍰"),
        (2, "Search Baked Goods 🔍"),
        (3, "Delete Baked Good ❌"),
        (4, "Return to Main Menu ⬅️")
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

def purchases_menu() -> bool:
    print()
    print(">>> Purchases Menu <<<")
    print("-----------------------")
    choice = prompt("Please select an option:", [
        (1, "Show All Purchases 💰"),
        (2, "Get Purchases By Date 🔍"),
        (3, "Get Most Frequent Purchase 🔍"),
        (4, "Return to Main Menu ⬅️")
    ])

    if choice == 1:
        show_all_purchases()
        return True
    elif choice == 2:
        get_purchases_by_date()
        return True
    elif choice == 3:
        get_most_frequent_purchase()
        return True
    else:
        return False

def customers_menu() -> bool:
    print()
    print(">>> Customers Menu <<<")
    print("----------------------")
    choice = prompt("Please select an option:", [
        (1, "Show All Customers 😋"),
        (2, "Add Customer ➕"),
        (3, "Return to Main Menu ⬅️")
    ])

    if choice == 1:
        show_customers()
        return True
    elif choice == 2:
        add_customer()
        return True
    else:
        return False

def main_menu() -> bool:
    print()
    print(">>> Main Menu <<<")
    print("-----------------")
    choice = prompt("Please select an option:", [
        (1, "Manage Customers 😋"),
        (2, "Manage Baked Goods 🍰"),
        (3, "Manage Ingredients 🥣"),
        (4, "Manage Purchases 💰"),
        (5, "Exit 🚪")
    ])

    if choice == 1:
        while customers_menu():
            pass
        return True
    elif choice == 2:
        while baked_goods_menu():
            pass
        return True
    elif choice == 3:
        while ingredients_menu():
            pass
        return True
    elif choice == 4:
        while purchases_menu():
            pass
        return True
    else:
        return False

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Express-O ☕ Point-of-Sale!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while main_menu():
        pass

if __name__ == "__main__":
    main()

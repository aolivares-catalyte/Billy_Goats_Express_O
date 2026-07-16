from services.purchase_service import PurchaseService
from repositories.purchase_repository import PurchaseRepository
from models.purchase import Purchase
from decimal import Decimal
from models.customer import Customer
from services.customer_service import CustomerService
from repositories.customer_repository import CustomerRepository
from models.drink import Drink
from models.ingredient import Ingredient
from datetime import datetime, timezone

purchase_service = PurchaseService(PurchaseRepository())
d= datetime(2020, 1, 1, tzinfo=timezone.utc)
beans=Ingredient(1, "Coffee Beans", Decimal("2.50"), 14.0, "g")
water=Ingredient(2, "Water", Decimal("0.01"), 250.0, "g")
milk=Ingredient(3, "Milk", Decimal("1.25"), 250.0, "g")
latte=Drink(2, "Latte", [beans, water, milk], Decimal("5.00"),Decimal("1.25") )
blueberry_muffin=Ingredient(2, "Water", Decimal("0.01"), 250.0, "g")
alex=Customer(99,"Alex","aolivares1042@gmail.com",Decimal("2000.00"))
alex_purchase = Purchase(120,[blueberry_muffin,latte],alex,d)
purchase_service.create_purchase(alex_purchase)

customer_service = CustomerService(CustomerRepository())
bill = Customer(1, "Bill Walters", "bill.walters@example.com", Decimal("560.78"))
customer_service.create_customer(bill)

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

def main_menu() -> bool:
    print("Welcome to Express-O Point-of-Sale!")
    choice = prompt("Please select an option:", [
        (1, "Show All Customers"),
        (2, "Add Customer"),
        (3, "Exit")
    ])

    if choice == 1:
        show_customers()
        return True
    elif choice == 2:
        add_customer()
        return True
    else:
        return False

def main():
    while main_menu():
        pass

if __name__ == "__main__":
    main()

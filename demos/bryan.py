from services.customer_service import CustomerService
from repositories.customer_repository import CustomerRepository
from models.customer import Customer
from decimal import Decimal

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
    print(f"Displaying Customers ({len(customers)}):")
    for customer in customers:
        print(customer)

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

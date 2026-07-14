from models.customer import Customer

class CustomerRepository:
    def __init__(self):
        self.customers: list[Customer] = []

    def get_all(self):
        return self.customers

    def get_by_id(self, id: int) -> Customer | None:
        return next((c for c in self.customers if c.id == id), None)

    def get_by_name(self, name: str) -> Customer | None:
        return next((c for c in self.customers if c.name == name), None)

    def add(self, customer: Customer) -> Customer:
        self.customers.append(customer)
        return customer

    def update(self, id: int, customer: Customer) -> Customer | None:
        customer_index = next((i for (i, c) in enumerate(self.customers) if c.id == id), None)
        if customer_index:
            self.customers[customer_index] = customer
            return customer
        else:
            return None

    def delete(self, id: int) -> bool:
        customer_index = next((i for (i, c) in enumerate(self.customers) if c.id == id), None)
        if customer_index is not None:
            self.customers.pop(customer_index)
            return True
        else:
            return False

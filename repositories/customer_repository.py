from models.customer import Customer

class CustomerRepository:
    def __init__(self):
        self.customers: list[Customer] = []

    def get_all(self):
        return self.customers

    def get_by_id(self, id: int) -> Customer | None:
        return next((c for c in self.customers if c.id == id), None)

    def get_by_name(self, name: str) -> Customer | None:
        return next((d for d in self.customers if d.name == name), None)

    def add(self, customer: Customer) -> Customer:
        self.customers.append(customer)
        return customer

    def update(self, id: int, customer: Customer) -> Customer | None:
        ix = None
        for i, customer in enumerate(self.customers):
            if id == customer.id:
                ix = i
        if ix:
            self.customers[ix] = customer
            return customer
        else:
            return None

    def delete(self, id: int) -> bool:
        ix = None
        for i, customer in enumerate(self.customers):
            if id == customer.id:
                ix = i
        if ix:
            self.customers.pop(ix)
            return True
        else:
            return False

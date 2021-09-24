# The Ice Cream Example
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoop(self, *new_scoops):
        self.scoops += new_scoops

    def flavors(self):
        return ", ".join(one_scoop.flavor for one_scoop in self.scoops)


# The Person and BankAccount Example
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = []

    def add_account(self, new_account):
        self.accounts.append(new_account)

    def all_balances(self):
        return [sum(one_account.transactions) for one_account in self.accounts]

    def current_total_balance(self):
        return sum(sum(one_account.transactions) for one_account in self.accounts)

    def average_transaction_amount(self):
        all_transactions = [one_transaction
                            for one_account in self.accounts
                            for one_transaction in one_account.transactions]

        return sum(all_transactions) / len(all_transactions)


class BankAccount:
    def __init__(self):
        self.transactions = []


# The Shopping Cart Example
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, name, price, new_quantity):
        if name in self.items:
            price, previous_quantity = self.items[name]
            self.items[name] = (price, previous_quantity + new_quantity)
        else:
            self.items[name] = (price, new_quantity)

    def remove(self, name):
        if name in self.items:
            price, quantity = self.items[name]
            if quantity == 1:
                del(self.items[name])
            else:
                self.items[name] = (price, quantity - 1)

    def total(self):
        return sum(price * quantity for price, quantity in self.items.values())

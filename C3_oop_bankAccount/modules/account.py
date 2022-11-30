import datetime

spacer = '\n\t\t\t'

nis_to_usd = 3.44


def convert_to_usd(nis: int, usd: float) -> float:
    return round(nis / usd, 2)


class BankAccount:
    def __init__(self, acc_number: str, holders=None, usd_accepted=False, limit=0, balance=0, transactions=None):
        self.acc_number = acc_number
        self.holders = holders
        self.usd_accepted = usd_accepted
        self.limit = limit
        self.balance = balance
        self.transactions = transactions

    def add_holder(self, holder_info: dict):
        if self.holders is None:
            self.holders = {}
        self.holders.update(holder_info)

    def usd_accepting(self) -> bool:
        return self.usd_accepted

    def get_balance(self) -> int:
        return self.balance

    def update_balance(self, new_balance: int):
        self.balance = new_balance

    def get_credit_limit(self) -> int:
        return self.limit

    def update_credit_limit(self, new_limit: int):
        self.limit = new_limit

    def get_transactions(self, *date) -> list:
        return self.transactions

    def update_transactions(self, data: dict):
        if self.transactions is None:
            self.transactions = []
        self.transactions.append(data)

    def __repr__(self) -> str:
        rep = f"""
        ACC: {self.acc_number}
        Credit Limit: {self.limit}
        Current Balance: {self.balance}₪ {"" if not self.usd_accepted else f"| {convert_to_usd(self.balance, nis_to_usd)}$"}
        USD: {"Not Applicable" if not self.usd_accepted else "Applicable"}
        Holders:
            {f'{spacer.join(f"{key}:{spacer}{spacer.join(map(str, value.items()))}" for key, value in self.holders.items()) if self.holders is not None else None}'}
        """
        return rep


class Holder:
    def __init__(self, holder_id: str, full_name: str, email: str, phone: str, address: dict):
        self.holder_id = holder_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address

    def data(self) -> dict:
        return {self.holder_id: {"full_name": self.full_name,
                                 "email": self.email,
                                 "phone": self.phone,
                                 "address": self.address}}


class Transaction:
    def __init__(self, account_obj: object, account_balance: int, transaction_type: str, amount: int):
        time = datetime.datetime.now()
        self.date = (time.strftime("%d.%m.%Y"), time.strftime("%H:%M:%S"))
        self.account_obj = account_obj
        self.account_balance = account_balance
        self.transaction_type = transaction_type
        self.amount = amount

    def transaction_handler(self):
        operation = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
        transaction_t = '+'
        compere = 0
        if self.transaction_type == "withdraw":
            compere = (self.account_balance - self.amount)
            transaction_t = '-'
        elif self.transaction_type == "deposit":
            if self.amount < 0:
                print("Can't deposit negative value.")
        if compere < 0:
            print("Inefficient amount.")
        else:
            new_balance = operation[transaction_t](self.account_balance, self.amount)
            self.account_obj.update_balance(new_balance)
            self.account_obj.update_transactions({self.date: {"type": self.transaction_type,
                                                              "amount": f'{transaction_t}{self.amount}₪',
                                                              "balance": f'{new_balance}₪{"" if not self.account_obj.usd_accepting() else f" | {convert_to_usd(new_balance, nis_to_usd)}$"}'}})

from modules.account import BankAccount, Holder, Transaction
import pprint

if __name__ == "__main__":

    holder1 = Holder(holder_id="20686",
                     full_name="Daniel Demidovski",
                     email="daniel@demidovski.dev",
                     phone="+972-523317877",
                     address={"country": "Israel", "city": "Netanya", "ZIP": "4655854"})

    holder2 = Holder(holder_id="46221",
                     full_name="Bob Testovich",
                     email="bob@testovich.dev",
                     phone="+972-525462541",
                     address={"country": "Poland", "city": "Warsaw", "ZIP": "112"})

    account = BankAccount("4145", usd_accepted=True, balance=1000)
    account.add_holder(holder1.data())
    account.add_holder(holder2.data())
    Transaction(account,
                int(account.get_balance()),
                transaction_type="withdraw",
                amount=100).transaction_handler()
    Transaction(account,
                int(account.get_balance()),
                transaction_type="deposit",
                amount=55000).transaction_handler()
    pprint.pprint(account.get_transactions())
    print(repr(account))
    print(account.holders)
    print(account.usd_accepted)

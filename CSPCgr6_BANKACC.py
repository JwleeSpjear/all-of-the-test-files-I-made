# first year college 2nd semester final project

import json
import sys
import os
from abc import ABC, abstractmethod

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "BankData.json")

MAX_ATTEMPTS = 2


# ── ABSTRACTION ──
class Transaction(ABC):

    @abstractmethod
    def execute(self, account):
        pass

    @abstractmethod
    def get_description(self):
        pass


# ── POLYMORPHISM ──
class DepositTransaction(Transaction):

    def __init__(self, amount):
        self.amount = amount

    def execute(self, account):
        if self.amount <= 0:
            print("Amount must be greater than zero.")
            return False
        account._balance += self.amount
        return True

    def get_description(self):
        return f"Deposit of ${self.amount:,.2f}"


class WithdrawTransaction(Transaction):

    def __init__(self, amount):
        self.amount = amount

    def execute(self, account):
        if self.amount <= 0:
            print("Amount must be greater than zero.")
            return False
        if self.amount > account._balance:
            print("Insufficient balance!")
            return False
        account._balance -= self.amount
        return True

    def get_description(self):
        return f"Withdrawal of ${self.amount:,.2f}"


class CheckTransaction(Transaction):

    def execute(self, account):
        print(f"  Your current balance: ${account._balance:,.2f}")
        return True

    def get_description(self):
        return "Balance Check"


# ── ENCAPSULATION ──
class BankAccount:

    def __init__(self, pin, balance=0.0):
        self._pin = str(pin)
        self._balance = float(balance)

    def get_pin(self):
        return self._pin

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = float(new_balance)

    @classmethod
    def load_all(cls):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
            return [cls(account["pin"], account["balance"]) for account in data["accounts"]]
        except FileNotFoundError:
            return []

    @classmethod
    def save_all(cls, accounts):
        with open(DATA_FILE, "w") as file:
            json.dump(
                {
                    "accounts": [
                        {"pin": acc.get_pin(), "balance": acc.get_balance()}
                        for acc in accounts
                    ]
                },
                file,
                indent=4
            )

    @classmethod
    def find_account(cls, pin, accounts):
        for account in accounts:
            if account.get_pin() == pin:
                return account
        return None

    @classmethod
    def pin_exists(cls, pin, accounts):
        return cls.find_account(pin, accounts) is not None


# ── INHERITANCE ──
class ATMachine(BankAccount):

    def __init__(self):
        super().__init__(pin="", balance=0.0)
        self.attempts = 0

    def authenticate(self):
        pin = input("Enter your PIN: ").strip()
        accounts = BankAccount.load_all()
        account = BankAccount.find_account(pin, accounts)

        if account:
            self.attempts = 0
            return account, accounts

        self.attempts += 1
        print(f"Invalid PIN! Attempt {self.attempts} of {MAX_ATTEMPTS}.")

        if self.attempts >= MAX_ATTEMPTS:
            print("Maximum attempts reached. Please try again later.")
            sys.exit()

        return None, None

    def ask_another(self):
        print()
        ans = input("Do you want to make another transaction? (y/n): ").strip().lower()
        if ans == "n":
            self.exit_atm()

    def check_balance(self):
        print("\n--- Check Balance ---")
        account, accounts = self.authenticate()
        if account:
            txn = CheckTransaction()
            txn.execute(account)
            print(f"  ({txn.get_description()})")
            self.ask_another()

    def do_withdraw(self):
        print("\n--- Withdraw ---")
        account, accounts = self.authenticate()
        if account:
            try:
                amount = float(input("Amount to withdraw: $"))
            except ValueError:
                print("Please enter a valid number.")
                return

            txn = WithdrawTransaction(amount)
            success = txn.execute(account)

            if success:
                target = BankAccount.find_account(account.get_pin(), accounts)
                target.set_balance(account.get_balance())
                BankAccount.save_all(accounts)
                print(f"  {txn.get_description()} was successful!")
                print(f"  Remaining balance: ${account.get_balance():,.2f}")

            self.ask_another()

    def do_deposit(self):
        print("\n--- Deposit ---")
        account, accounts = self.authenticate()
        if account:
            try:
                amount = float(input("Amount to deposit: $"))
            except ValueError:
                print("Please enter a valid number.")
                return

            txn = DepositTransaction(amount)
            success = txn.execute(account)

            if success:
                target = BankAccount.find_account(account.get_pin(), accounts)
                target.set_balance(account.get_balance())
                BankAccount.save_all(accounts)
                print(f"  {txn.get_description()} was successful!")
                print(f"  New total balance: ${account.get_balance():,.2f}")

            self.ask_another()

    def add_account(self):
        print("\n--- Add New Account ---")
        new_pin = input("Enter new PIN: ").strip()
        accounts = BankAccount.load_all()

        if BankAccount.pin_exists(new_pin, accounts):
            print("PIN already exists. Please choose a different one.")
            return

        try:
            start_balance = float(input("Enter opening balance (press Enter for 0): ") or 0)
        except ValueError:
            start_balance = 0.0

        new_account = BankAccount(new_pin, start_balance)
        accounts.append(new_account)
        BankAccount.save_all(accounts)
        print("New account created successfully!")

    def delete_account(self):
        print("\n--- Delete Account ---")
        account, accounts = self.authenticate()
        if account:
            confirm = input("Are you sure you want to delete this account? (yes/no): ").strip().lower()
            if confirm == "yes":
                accounts = [acc for acc in accounts if acc.get_pin() != account.get_pin()]
                BankAccount.save_all(accounts)
                print("Account deleted successfully.")
                self.exit_atm()
            else:
                print("Deletion cancelled.")

    def view_all_accounts(self):
        print("\n--- All Accounts ---")
        accounts = BankAccount.load_all()
        if not accounts:
            print("No accounts found.")
            return
        print(f"  Total accounts: {len(accounts)}")
        print("  " + "-" * 30)
        for i, acc in enumerate(accounts, start=1):
            hidden_pin = "*" * (len(acc.get_pin()) - 2) + acc.get_pin()[-2:]
            print(f"  [{i}] PIN: {hidden_pin}  |  Balance: ${acc.get_balance():,.2f}")
        print()

    @staticmethod
    def exit_atm():
        print("\nThank you for using the ATM machine. Goodbye!")
        sys.exit()

    def run(self):
        actions = {
            "1": ("Check Balance",     self.check_balance),
            "2": ("Withdraw",          self.do_withdraw),
            "3": ("Deposit",           self.do_deposit),
            "4": ("Add Account",       self.add_account),
            "5": ("Delete Account",    self.delete_account),
            "6": ("View All Accounts", self.view_all_accounts),
            "7": ("Exit",              self.exit_atm),
        }

        while True:
            print("\nWelcome to the ATM Machine")
            print("=" * 46)
            for key, (label, _) in actions.items():
                print(f"  [{key}] {label}")
            print("=" * 46)

            choice = input("Select Option: ").strip()
            action_entry = actions.get(choice)

            if action_entry:
                _, action_func = action_entry
                action_func()
            else:
                print("Invalid option. Please select 1-7.")


if __name__ == "__main__":
    atm = ATMachine()
    atm.run()

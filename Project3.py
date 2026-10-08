from abc import ABC, abstractmethod
import csv
import os


# ==========================================================
# 1. ABSTRACT BASE CLASS
# ==========================================================
class Account(ABC):

    def __init__(self, account_number, account_holder_name, account_balance):

        # Encapsulation - Private Attributes
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

        self.transactions_history = []

    # ---------------- GETTERS ----------------

    def get_account_number(self):
        return self.__account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def get_balance(self):
        return self.__account_balance

    # ---------------- SETTER ----------------

    def set_balance(self, balance):
        self.__account_balance = balance

    # ---------------- DISPLAY ----------------

    def display_account_details(self):
        print("\n===== Account Details =====")
        print("Account Number:", self.__account_number)
        print("Account Holder Name:", self.__account_holder_name)
        print("Account Balance:", self.__account_balance)
        print("Account Type:", self.account_type())

    # Abstraction
    @abstractmethod
    def account_type(self):
        pass


# ==========================================================
# 2. DERIVED CLASS - INHERITANCE
# ==========================================================
class SavingAccount(Account):

    def account_type(self):
        return "Saving Account"


# ==========================================================
# 3. BANK ACCOUNT MANAGEMENT CLASS
# ==========================================================
class Bank_Account_Management:

    def __init__(self):
        self.accounts = []

    # ------------------------------------------------------
    # CREATE ACCOUNT
    # ------------------------------------------------------
    def create_account(self):

        account_number = input("Enter The Account Number: ")

        # Check duplicate account number
        for account in self.accounts:

            if account.get_account_number() == account_number:
                print("Account Number Already Exists...")
                return

        account_holder_name = input("Enter The Account Holder Name: ")

        try:
            account_balance = float(
                input("Enter The Account Balance: ")
            )

            if account_balance < 0:
                print("Balance Cannot Be Negative...")
                return

        except ValueError:
            print("Please Enter Valid Amount.")
            return

        # Create object of derived class
        account = SavingAccount(
            account_number,
            account_holder_name,
            account_balance
        )

        self.accounts.append(account)

        print("Account Created Successfully...")

    # ------------------------------------------------------
    # DEPOSIT MONEY
    # ------------------------------------------------------
    def deposit_money(self):

        account_number = input("Enter The Account Number: ")

        for account in self.accounts:

            if account.get_account_number() == account_number:

                try:
                    deposit_amount = float(
                        input("Enter The Amount You Want To Deposit: ")
                    )

                    if deposit_amount <= 0:
                        print(
                            "Deposit Amount Must Be Greater Than Zero..."
                        )
                        return

                except ValueError:
                    print("Please Enter Valid Amount.")
                    return

                # Update balance using getter and setter
                new_balance = (
                    account.get_balance() + deposit_amount
                )

                account.set_balance(new_balance)

                # Save transaction
                account.transactions_history.append(
                    "+" + str(deposit_amount)
                )

                print(
                    f"{deposit_amount} Deposited Successfully."
                )

                print(
                    f"Available Balance Is "
                    f"{account.get_balance()}."
                )

                return

        print("Account Not Found...")

    # ------------------------------------------------------
    # WITHDRAW MONEY
    # ------------------------------------------------------
    def withdraw_money(self):

        account_number = input("Enter The Account Number: ")

        for account in self.accounts:

            if account.get_account_number() == account_number:

                try:
                    withdraw_amount = float(
                        input("Enter The Amount You Want To Withdraw: ")
                    )

                    if withdraw_amount <= 0:
                        print(
                            "Withdraw Amount Must Be Greater Than Zero..."
                        )
                        return

                except ValueError:
                    print("Please Enter Valid Amount.")
                    return

                # Check balance
                if withdraw_amount > account.get_balance():

                    print("Insufficient Balance...")
                    return

                # Update balance
                new_balance = (
                    account.get_balance() - withdraw_amount
                )

                account.set_balance(new_balance)

                # Add transaction
                account.transactions_history.append(
                    "-" + str(withdraw_amount)
                )

                print(
                    f"{withdraw_amount} Withdrawn Successfully."
                )

                print(
                    f"Available Balance Is "
                    f"{account.get_balance()}."
                )

                return

        print("Account Not Found...")

    # ------------------------------------------------------
    # CHECK BALANCE
    # ------------------------------------------------------
    def check_balance(self):

        account_number = input("Enter The Account Number: ")

        for account in self.accounts:

            if account.get_account_number() == account_number:

                print(
                    "Available Balance =",
                    account.get_balance()
                )

                return

        print("Account Not Found...")

    # ------------------------------------------------------
    # TRANSACTION HISTORY
    # ------------------------------------------------------
    def transaction_history(self):

        account_number = input("Enter The Account Number: ")

        for account in self.accounts:

            if account.get_account_number() == account_number:

                print("\n===== Transaction History =====")

                if len(account.transactions_history) == 0:

                    print("No Transactions Found.")

                else:

                    for transaction in account.transactions_history:
                        print(transaction)

                return

        print("Account Not Found...")

    # ------------------------------------------------------
    # DISPLAY ACCOUNT DETAILS
    # ------------------------------------------------------
    def display_account(self):

        account_number = input("Enter The Account Number: ")

        for account in self.accounts:

            if account.get_account_number() == account_number:

                account.display_account_details()
                return

        print("Account Not Found...")

    # ------------------------------------------------------
    # SAVE RECORD TO FILE
    # ------------------------------------------------------
    def save_record(self):

        try:

            with open("account.csv", "w") as ac:

                for account in self.accounts:

                    transactions = "|".join(
                        account.transactions_history
                    )

                    ac.write(
                        account.get_account_number()
                        + ","
                        + account.get_account_holder_name()
                        + ","
                        + str(account.get_balance())
                        + ","
                        + transactions
                        + "\n"
                    )

            print("Data Saved Successfully...")

        except OSError:
            print("Error While Saving File...")

    # ------------------------------------------------------
    # LOAD RECORD FROM FILE
    # ------------------------------------------------------
    def load_record(self):

        try:

            with open("account.csv", "r") as ac:

                for line in ac:

                    line = line.strip()

                    if not line:
                        continue

                    data = line.split(",", 3)

                    # Invalid record protection
                    if len(data) < 3:
                        continue

                    account_number = data[0]
                    account_holder_name = data[1]

                    try:
                        account_balance = float(data[2])
                    except ValueError:
                        continue

                    # Create account object
                    account = SavingAccount(
                        account_number,
                        account_holder_name,
                        account_balance
                    )

                    # Load transaction history
                    if len(data) == 4 and data[3]:

                        account.transactions_history = (
                            data[3].split("|")
                        )

                    self.accounts.append(account)

            print("Previous Data Loaded Successfully...")

        except FileNotFoundError:
            # First time running program
            print("No Previous Record Found.")

        except OSError:
            print("Error While Reading File...")


# ==========================================================
# MAIN PROGRAM
# ==========================================================

system = Bank_Account_Management()

# Load previous account records
system.load_record()


while True:

    print("\n===== Bank Account Management System =====")

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Display Account Details")
    print("7. Save Data")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        system.create_account()

    elif choice == "2":
        system.deposit_money()

    elif choice == "3":
        system.withdraw_money()

    elif choice == "4":
        system.check_balance()

    elif choice == "5":
        system.transaction_history()

    elif choice == "6":
        system.display_account()

    elif choice == "7":
        system.save_record()

    elif choice == "8":

        # Automatically save before exit
        system.save_record()

        print("Exit Program...")
        break

    else:
        print("Invalid Input...")

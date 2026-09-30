# operations.py

def check_balance(balance):
    print("\nCurrent Balance\t\t: ₱ {:,.2f}".format(balance))


def deposit(balance):
    while True:
        try:
            amount = float(input("\nEnter Deposit Amount\t: ₱ "))

            if amount <= 0:
                print("Deposit amount must be greater than ₱ 0.00.")
            else:
                balance += amount
                print("Deposit Successfully!")
                return balance

        except ValueError:
            print("Invalid input! Please enter a valid amount.")


def withdraw(balance):
    while True:
        try:
            amount = float(input("\nEnter Withdrawal Amount\t: ₱ "))

            if amount <= 0:
                print("Withdrawal amount must be greater than ₱ 0.00.")

            elif amount > balance:
                print("Insufficient balance!")

            else:
                balance -= amount
                print("Withdraw Successfully!")
                return balance

        except ValueError:
            print("Invalid input! Please enter a valid amount.")
# account.py

def get_name():
    return input("Enter Name\t: ")


def get_initial_balance():
    while True:
        try:
            balance = float(input("Enter Balance\t: ₱ "))

            if balance < 0:
                print("Balance cannot be negative.")
            else:
                return balance

        except ValueError:
            print("Invalid input! Please enter a valid amount.")
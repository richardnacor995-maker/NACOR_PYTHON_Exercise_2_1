# main.py

from account import get_name, get_initial_balance
from operations import check_balance, deposit, withdraw


print("================================")
print("          ATM MACHINE")
print("================================")

# Get user information
name = get_name()
balance = get_initial_balance()

print("\nWelcome, {}!".format(name))

while True:

    print("\n")
    print("      * * * A T M * * *")
    print("       Bank Operation:")
    print()
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("\nChoose Operation: ")

    # Check Balance
    if choice == "1":
        check_balance(balance)

    # Deposit
    elif choice == "2":
        balance = deposit(balance)

    # Withdraw
    elif choice == "3":
        balance = withdraw(balance)

    # Exit
    elif choice == "4":
        print("\nThank you for choosing our bank!")
        print("Have a nice day!")
        break

    # Invalid operation
    else:
        print("\nInvalid operation! Please choose between 1 and 4.")
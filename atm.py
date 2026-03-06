balance = 5000
pin = 1234
transactions = []
account_holder = "John Doe"
account_number = "XXXX-XXXX-1234"

def check_balance():
    print(f"\nYour current balance is: ₹{balance}")


def deposit():
    global balance
    amount = int(input("\nEnter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: ₹{amount}")
        print(f"₹{amount} deposited successfully. New balance: ₹{balance}")
    else:
        print("Invalid amount.")


def withdraw():
    global balance
    amount = int(input("\nEnter amount to withdraw: ₹"))
    if amount > balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Invalid amount.")
    else:
        balance -= amount
        transactions.append(f"Withdrew: ₹{amount}")
        print(f"₹{amount} withdrawn successfully. New balance: ₹{balance}")


def change_pin():
    global pin
    old = int(input("\nEnter current PIN: "))
    if old == pin:
        new = int(input("Enter new PIN: "))
        pin = new
        print("PIN changed successfully.")
    else:
        print("Incorrect PIN.")


def account_info():
    print(f"\n--- Account Information ---")
    print(f"Account Holder : {account_holder}")
    print(f"Account Number : {account_number}")
    print(f"Current Balance: ₹{balance}")


def exit_account():
    print("\nThank you for using the ATM. Goodbye!")


def main():
    print("Welcome to the ATM")
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin != pin:
        print("Wrong PIN. Access denied.")
        return

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Account Info")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            account_info()
        elif choice == "6":
            exit_account()
            break
        else:
            print("Invalid option. Try again.")


main()

balance = 5000
pin = 1234


def check_balance():
    print(f"\nYour current balance is: ₹{balance}")


def deposit():
    global balance
    amount = int(input("\nEnter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
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
        print("5. Exit")
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
            exit_account()
            break
        else:
            print("Invalid option. Try again.")


main()

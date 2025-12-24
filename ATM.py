class ATM:
    def __init__(self):
        self.name = ""
        self.mobile = ""
        self.pin = ""
        self.balance = 0
        self.transactions = []

    # ---------- Card Activation ----------
    def activate_card(self):
        print("\n--- ATM Card Activation ---")

        # Name validation
        while True:
            self.name = input("Enter your full name: ").strip()
            if self.name.replace(" ", "").isalpha():
                break
            print("Invalid name. Use alphabets only.")

        # Mobile number validation
        while True:
            self.mobile = input("Enter 10-digit mobile number: ")
            if self.mobile.isdigit() and len(self.mobile) == 10:
                break
            print("Invalid mobile number.")

        # PIN creation
        while True:
            pin1 = input("Create a 4-digit PIN: ")
            pin2 = input("Re-enter PIN: ")
            if pin1 == pin2 and pin1.isdigit() and len(pin1) == 4:
                self.pin = pin1
                break
            print("PIN mismatch or invalid PIN.")

        # Initial deposit
        while True:
            try:
                amount = int(input("Initial deposit (minimum ₹1000): "))
                if amount >= 1000:
                    self.balance = amount
                    self.transactions.append(f"Deposited ₹{amount}")
                    print("Card activated successfully!")
                    break
                else:
                    print("Minimum deposit is ₹1000.")
            except ValueError:
                print("Enter a valid amount.")

    # ---------- PIN Verification ----------
    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    # ---------- Change PIN ----------
    def change_pin(self):
        if self.verify_pin():
            while True:
                new_pin = input("Enter new 4-digit PIN: ")
                confirm_pin = input("Confirm new PIN: ")
                if new_pin == confirm_pin and new_pin.isdigit() and len(new_pin) == 4:
                    self.pin = new_pin
                    print("PIN changed successfully.")
                    return
                print("PIN mismatch or invalid.")
        else:
            print("Incorrect PIN.")

    # ---------- Deposit ----------
    def deposit(self):
        if self.verify_pin():
            try:
                amount = int(input("Enter deposit amount: "))
                if amount > 0:
                    self.balance += amount
                    self.transactions.append(f"Deposited ₹{amount}")
                    print(f"₹{amount} deposited successfully.")
                else:
                    print("Invalid amount.")
            except ValueError:
                print("Enter a valid number.")
        else:
            print("Incorrect PIN.")

    # ---------- Withdrawal ----------
    def withdraw(self):
        if self.verify_pin():
            try:
                amount = int(input("Enter withdrawal amount: "))
                charge = self.calculate_charge(amount)
                total = amount + charge

                if total <= self.balance and amount > 0:
                    self.balance -= total
                    self.transactions.append(
                        f"Withdrew ₹{amount} (Charge ₹{charge})"
                    )
                    print(f"₹{amount} withdrawn successfully.")
                    print(f"Transaction charge: ₹{charge}")
                else:
                    print("Insufficient balance or invalid amount.")
            except ValueError:
                print("Enter a valid number.")
        else:
            print("Incorrect PIN.")

    # ---------- Transaction Charge ----------
    def calculate_charge(self, amount):
        if amount <= 1000:
            return 0
        elif amount <= 20000:
            return 100
        elif amount <= 100000:
            return 1000
        else:
            return 2000

    # ---------- Balance ----------
    def check_balance(self):
        if self.verify_pin():
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("Incorrect PIN.")

    # ---------- Transaction History ----------
    def show_transactions(self):
        if self.verify_pin():
            print("\n--- Last Transactions ---")
            for txn in self.transactions[-10:]:
                print(txn)
        else:
            print("Incorrect PIN.")

    # ---------- Main Menu ----------
    def menu(self):
        while True:
            print("""
--- ATM Menu ---
1. Change PIN
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. View Last 10 Transactions
6. Exit
""")
            choice = input("Choose an option: ")

            if choice == "1":
                self.change_pin()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                self.show_transactions()
            elif choice == "6":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice.")


# ---------- Demonstration ----------
if __name__ == "__main__":
    atm = ATM()
    atm.activate_card()
    atm.menu()

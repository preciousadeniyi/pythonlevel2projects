import re
import random
import string
from database import Database
from decimal import Decimal

class BankAccount:
    

    def __init__(self):
        self.db = Database()

    def signup(self):
        

        print("Welcome to our bank! Let's create your account.")
        
       
        while True:
            username = input("Enter your username: ")
            if self.validate_username(username):
                break
            else:
                print("Invalid username format. Username must contain only alphanumeric characters and be between 4 and 20 characters long.")

        
        while True:
            email = input("Enter your email address: ")
            if self.validate_email(email):
                break
            else:
                print("Invalid email format. Please enter a valid email address.")

       
        while True:
            phone_number = input("Enter your phone number: ")
            if self.validate_phone_number(phone_number):
                break
            else:
                print("Invalid phone number format. Please enter a valid Nigerian phone number.")

        
        password = self.generate_password()

        
        self.db.add_user(username, email, phone_number, password)

        print("Your account has been successfully created.")
        print(f"Your password is: {password}")

    def login(self):
        

        print("Welcome back! Please log in to your account.")
        phone_number = input("Enter your phone number: ")
        password = input("Enter your password: ")

        if self.db.authenticate_user(phone_number, password):
            print("Login successful!")
            user_id = self.get_user_id(phone_number)
            self.show_menu(user_id)
        else:
            print("Invalid phone number or password.")

    def show_menu(self, user_id):
       

        while True:
            print("\nMain Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Edit Account")
            print("6. Pay Bills")
            print("7. View Transactions")
            print("8. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.deposit(user_id)
            elif choice == '2':
                self.withdraw(user_id)
            elif choice == '3':
                self.transfer(user_id)
            elif choice == '4':
                self.check_balance(user_id)
            elif choice == '5':
                self.edit_account(user_id)
            elif choice == '6':
                self.pay_bills(user_id)
            elif choice == '7':
                self.view_transactions(user_id)
            elif choice == '8':
                print("Thank you for using our bank. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def deposit(self, user_id):
            

            amount_str = input("Enter the amount to deposit: ")

            try:
                amount = Decimal(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                return

            if not self.db.user_exists(user_id):
                print("User not found.")
                return

            current_balance = self.db.get_balance(user_id)
            if current_balance is not None:
                new_balance = current_balance + amount
                self.db.update_balance(user_id, new_balance)
                print("Deposit successful! Your money has been deposited.")
            else:
                print("User not found.")

    def withdraw(self, user_id):
        

        amount_str = input("Enter the amount to withdraw: ")
        try:
            amount = Decimal(amount_str)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return

        current_balance = self.db.get_balance(user_id)
        if current_balance is not None:
            if current_balance >= amount:
                new_balance = current_balance - amount
                self.db.update_balance(user_id, new_balance)
                print("Withdrawal successful!")
            else:
                print("Insufficient balance.")
        else:
            print("User not found.")

    def transfer(self, sender_user_id):
           

            recipient_phone_number = input("Enter recipient's phone number: ")
            amount_str = input("Enter the amount to transfer: ")
            try:
                amount = Decimal(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                return

            sender_balance = self.db.get_balance(sender_user_id)

            if sender_balance is not None:
                if sender_balance >= amount:
                    recipient_user_id = self.get_user_id(recipient_phone_number)
                    if recipient_user_id is not None:
                        if recipient_user_id != sender_user_id:  # Check if recipient is not the sender
                            recipient_balance = self.db.get_balance(recipient_user_id)
                            if recipient_balance is not None:
                                sender_new_balance = sender_balance - amount
                                recipient_new_balance = Decimal(recipient_balance) + amount
                                self.db.update_balance(sender_user_id, sender_new_balance)
                                self.db.update_balance(recipient_user_id, recipient_new_balance)
                                print("Transfer successful!")
                            else:
                                print("Recipient's account not found.")
                        else:
                            print("Transfer to your own account is not allowed.")
                    else:
                        print("Recipient's account not found.")
                else:
                    print("Insufficient balance.")
            else:
                print("User not found.")



    def check_balance(self, user_id):
        

        balance = self.db.get_balance(user_id)
        if balance is not None:
            print(f"Your current balance is: {balance}")
        else:
            print("User not found.")

    def edit_account(self, user_id):
        

        print("Edit Account:")
        print("1. Change Password")
        print("2. Update Email")
        print("3. Update Phone Number")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_password = input("Enter new password: ")
            self.db.change_password(user_id, new_password)
            print("Password updated successfully!")
        elif choice == '2':
            new_email = input("Enter new email address: ")
            self.db.update_email(user_id, new_email)
            print("Email updated successfully!")
        elif choice == '3':
            new_phone_number = input("Enter new phone number: ")
            if self.validate_phone_number(new_phone_number):
                self.db.update_phone_number(user_id, new_phone_number)
                print("Phone number updated successfully!")
            else:
                print("Invalid phone number format. Please enter a valid Nigerian phone number.")
        else:
            print("Invalid choice.")

    def pay_bills(self, user_id):
        
        print("Feature coming soon!")

    def view_transactions(self, user_id):
       

        transactions = self.db.get_transactions(user_id)
        if transactions:
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions found.")

    def validate_username(self, username):
       

        return 4 <= len(username) <= 20 and username.isalnum()

    def validate_email(self, email):
        

        pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        return bool(re.match(pattern, email))
    
    def validate_phone_number(self, phone_number):
            '''Validates Nigerian phone number format'''

            pattern = r"^(?:\+?234)?(?:70|80|90|81)\d{8}$"
            return bool(re.match(pattern, phone_number))

    def generate_password(self):
       

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(12))
        return password

    def get_user_id(self, phone_number):
      

        return self.db.get_user_id(phone_number)

def main():
    bank = BankAccount()

    while True:
        print("\nWelcome to Our Bank")
        print("1. Sign Up")
        print("2. Login")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bank.signup()
        elif choice == '2':
            bank.login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

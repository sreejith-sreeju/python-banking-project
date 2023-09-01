class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}")

    def display_balance(self):
        print(f"Current balance is {self.balance}")

#entering datas:
customer_name = input("Enter your name: ")
initial_balance = float(input("Enter initial deposit amount: "))

customer_account = BankAccount(customer_name, initial_balance)

print("Account created successfully!")
customer_account.display_balance()

# depositing  money
deposit_amount = float(input("Enter deposit amount: "))
customer_account.deposit(deposit_amount)

# withdrawing money
withdraw_amount = float(input("Enter withdrawal amount: "))
customer_account.withdraw(withdraw_amount)

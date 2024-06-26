class Bank:
    def __init__(self):
        self.account = {}

    def create_account(self, account_number, holder_name, initial_balance):
        if account_number in self.account:
            return "account already exist"

        if initial_balance < 2500:
            return "deposit amount must be 2500 or more"

        self.account[account_number] = {
            "holder_name": holder_name,
            "amount": initial_balance,
        }
        return "account created successfully"

    def deposit_money(self, account_number, withdraw_amount):
        if account_number not in self.account:
            return "account does not exist"

        if withdraw_amount <= 0:
            return "diposit amount not be zero or negative"

        self.account[account_number]["amount"] = (
            self.account[account_number]["amount"] + deposit_amount
        )
        return "deposit amount succesfully"

    def withdraw_money(self, account_number, withdraw_amount):
        if account_number not in self.account:
            return "account does not exist"

        if withdraw_amount <= 0:
            return "withdraw amount not be zero or negative"

        self.account[account_number]["amount"] = (
            self.account[account_number]["amount"] - withdraw_amount
        )
        return "withdraw amount succesfully"

    def check_balance(self, account_number):
        if account_number not in self.account:
            return "account does not exist"

        return self.account[account_number]["amount"]

    def money_transfer(self, sender_account_no, receiver_account_no, amount):
        if sender_account_no not in self.account:
            return "sender acount does not exist"

        if receiver_account_no not in self.account:
            return "receiver acount does not exist"

        self.account[sender_account_no]["amount"] = (
            self.account[sender_account_no]["amount"] - amount
        )
        self.account[receiver_account_no]["amount"] = (
            self.account[receiver_account_no]["amount"] + amount
        )
        return "money transfer successfully"

    
    def list_of_account(self):
        return self.account.keys()


bank = Bank()


while True:
    print("\n****** Bank Management System ******")
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. List of accounts")
    print("7. Exit")
    choice = input("\nEnter your Choice (1 to 7): ")

    if choice == "1":
        account_number = int(input("Enter account number: "))
        holder_name = input("Enter account holder name: ")
        initial_balance = int(input("Enter deposit amount: "))
        result = bank.create_account(account_number, holder_name, initial_balance)
        print(result)

    elif choice == "2":
        account_number = int(input("Enter account number: "))
        deposit_amount = int(input("Enter deposit amount: "))
        result = bank.deposit_money(account_number, deposit_amount)
        print(result)

    elif choice == "3":
        account_number = int(input("Enter account number: "))
        withdraw_amount = int(input("Enter withdraw amount: "))
        result = bank.withdraw_money(account_number, withdraw_amount)
        print(result)

    elif choice == "4":
        account_number = int(input("Enter account number: "))
        result = bank.check_balance(account_number)
        print(result)

    elif choice == "5":
        sender_account_no = int(input("Enter sender account number: "))
        receiver_account_no = int(input("Enter receiver account number: "))
        amount = int(input("Enter transfer amount: "))
        result = bank.money_transfer(sender_account_no, receiver_account_no, amount)
        print(result)

    elif choice == "6":
        result = bank.list_of_account()
        print(result)

    else:
        break

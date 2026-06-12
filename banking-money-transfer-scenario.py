class BankAccount:
    def __init__(self, account_number):
        self.account_number = str(account_number)
        self.balance = 0

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds")

    def deposit(self, amount):
        self.balance += amount

def transfer_amount(acc_1, acc_2, amount):  
    try:
        acc_1.withdraw(amount)
        acc_2.deposit(amount)
        return True
    except ValueError as e:
        print(str(e))  
        return False

user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(30)
user_2.deposit(100)

print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))
is_successful = transfer_amount(user_1, user_2, 50)
print(is_successful)
if is_successful:
    print("Transferring 50/- from User 1 to User 2")
    print("User 1 Balance: {}/-".format(user_1.get_balance()))
    print("User 2 Balance: {}/-".format(user_2.get_balance()))
class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("{} deposited {} amount".format(self.owner, amount))


    def withdraw(self, amount):
        if amount > self.balance:
            return 'balance not available'
        self.balance = self.balance - amount
        print("{} withdraw {} amount".format(self.owner, amount))

    def __str__(self):
        return 'balance : {} owner : {}'.format(self.balance, self.owner)



my_account = Account('bhagya',500)
print(my_account)
#Deposit money
my_account.deposit(200)
#Withdraw money
print(my_account.withdraw(800))

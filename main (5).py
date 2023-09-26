class bank_account:
def--=-_init_(self,account_number,account_holer_name,initial_balance=0.0):
  self.__account_number=account_number
  self.__acount_holer_name=account_holer_name
  self.__account_balance=initial_balance
def deposite(self,amount):
  if amount > 0:
    self.__account_balance+=amount 
    print("deposit${}.new balance): ${}".format(amount,self.__account_balance)
                                     else:
print("Invaid deposit amount.please depoite a positive amount.")

def withdraw(self,amount):
  if amount > 0 and amount < = self.__account_balance:
    self.__account_balance==amount
    print("withdraw${}.new balance:
    ${}".format(amount,self.__account_balance))
    else:
    print("Invaild withdraw amount of insufficient n=balance.")

    def display_balance(self):
    print("Account balance for{} (account#{}):${}".format(self.__account_holder_name,self.__account_balance))
    
account==Bankaccount(account_number="345777453875",account_holder_name=vasuki,initial_balance=500.0)
    account.display_balance()
    account.deposit(500.0)
    account.withdraw(200.0)
    account.display_balance()
  
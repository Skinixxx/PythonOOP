class BankAccount:
    def __init__(self,owner,balance=0):
        self.__owner = owner
        self.__balance = max(balance,0)

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение суммой: {amount}. Баланс: {self.__balance}")
        else:
            print(f"Сумма не положительна")
    
    def withdraw(self,amount):
        if (self.__balance - amount)>=0:
            self.__balance -= amount
            print(f"Снятие:{amount}. Баланс: {self.__balance}")
        else:
            print("Недостаточно средств")

test = BankAccount("Иван",100)
test.withdraw(200)
test.deposit(300)
test.withdraw(400)
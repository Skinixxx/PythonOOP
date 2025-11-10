class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = max(balance,0)

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение суммой: {amount}. Баланс: {self.balance}")
        else:
            print(f"Сумма должна быть положительной")
    
    def withdraw(self,amount):
        if (self.balance - amount)>=0:
            self.balance -= amount
            print(f"Снятие:{amount}. Баланс: {self.balance}")
        else:
            print("Недостаточно средств")

test = BankAccount("Иван",100)
test.withdraw(200)
test.deposit(300)
test.withdraw(400)
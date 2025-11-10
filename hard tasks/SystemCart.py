class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self,product:Product,quantity = 1):
        self.items.append({'product':product,'quantity':quantity})

    def total(self):
        return sum(item['product'].price*item['quantity'] for item in self.items)
    def __str__(self):
        return ''.join([f"{item['product'].name}: {item['quantity']}; " for item in self.items])

p1 = Product("Яблоко",50)
p2 = Product("Хлеб",30)
cart = Cart()
cart.add_product(p1,2)
cart.add_product(p2,3)
print(cart)
print(f"Сумма: {cart.total()} руб")
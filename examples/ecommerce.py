class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity=1):
        if self.stock < quantity:
            raise ValueError("Insufficient stock")
        self.stock -= quantity


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, product, quantity=1):
        self.cart.append((product, quantity))

    def remove_from_cart(self, product):
        for item in self.cart:
            if item[0] == product:
                self.cart.remove(item)
                return
        raise ValueError("Product not found in cart")

    def checkout(self):
        order = Order(self.cart)
        self.cart = []
        return order


class Order:
    def __init__(self, cart):
        self.products = []
        self.total = 0
        for item in cart:
            product, quantity = item
            if product.stock < quantity:
                raise ValueError("Insufficient stock")
            product.purchase(quantity)
            self.products.append((product, quantity))
            self.total += product.price * quantity


class Payment:
    def __init__(self, order, amount):
        self.order = order
        self.amount = amount

    def process(self):
        if self.amount != self.order.total:
            raise ValueError("Incorrect payment amount")

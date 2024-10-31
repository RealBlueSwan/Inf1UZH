class Product:
    def __init__(self, product, price, discount):
        self.product = product
        self.price = price
        self.discount = discount

    def sales_price(self):
        return round((1 - self.discount) * self.price, 2)

    def __str__(self):
        return f"{self.product} sells for {self.sales_price()}"
    
    def __repr__(self):
        return f"Product({self.product}, {self.price:.2f}, {self.discount:.2f})"


p = Product("Smartphone", 1000, 0.1)
print( p.sales_price() )                    # 900.0
print( p )                                  # Smartphone sells for 900.00
print( [p, Product("Dumbphone", 100, 0.2)]) # [Product(Smartphone, 1000.00, 0.10), Product(Dumbphone, 100.00, 0.20)]
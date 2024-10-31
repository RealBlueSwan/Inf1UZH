

class Product:
    def __init__(self, product, price, discount):
        self.product = product
        self.price = price
        self.discount = discount

    def __str__(self):
        return f"{self.product} sells for {self.sales_price()}"
        
    def __repr__(self):
        return f"Product({self.product}, {self.price}, {self.discount})"

    def sales_price(self):
        return self.price * (1-self.discount)
        
# The following example illustrates how the solution may be used:

p = Product("Smartphone", 1000, 0.1)
print( p.sales_price() )                        # 900.0
print( p )                                      # Smartphone sells for 900.00
print( [p, Product("Dumbphone", 100, 0.2)])     # [Product(Smartphone, 1000.00, 0.10), Product(Dumbphone, 100.00, 0.20)]
# The code above should produce the following output:




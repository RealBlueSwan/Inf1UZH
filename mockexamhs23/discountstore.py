class Product:
    pass


p = Product("Smartphone", 1000, 0.1)
print( p.sales_price() )
print( p )
print( [p, Product("Dumbphone", 100, 0.2)])


# 900.0
# Smartphone sells for 900.00
# [Product(Smartphone, 1000.00, 0.10), Product(Dumbphone, 100.00, 0.20)]
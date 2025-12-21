from util.file_manager import CSVFileManager
from util.converter import CashierConverter, CustomerConverter, ProductConverter
from orders.order import *
"""
# ===== PROBAR CASHIERS =====
print("=== CASHIERS ===")
fm_cashiers = CSVFileManager("data/cashiers.csv")
df_cashiers = fm_cashiers.read()

cashier_converter = CashierConverter()
cashiers = cashier_converter.convert(df_cashiers)
cashier_converter.print(cashiers)


# ===== PROBAR CUSTOMERS =====
print("\n=== CUSTOMERS ===")
fm_customers = CSVFileManager("data/customers.csv")
df_customers = fm_customers.read()

customer_converter = CustomerConverter()
customers = customer_converter.convert(df_customers)
customer_converter.print(customers)


# ===== PROBAR PRODUCTS =====
print("\n=== DRINKS ===")
fm_drinks = CSVFileManager("data/drinks.csv")
df_drinks = fm_drinks.read()

product_converter = ProductConverter()
drinks = product_converter.convert(df_drinks, "drink")
product_converter.print(drinks)


print("\n=== HAPPY MEALS ===")
fm_happy = CSVFileManager("data/happyMeal.csv")
df_happy = fm_happy.read()

happy_meals = product_converter.convert(df_happy, "happy_meal")
product_converter.print(happy_meals)
"""
from products.product import Drink, Hamburger, Soda, HappyMeal, Product
from products.food_package import Wrapping, Glass, Bottle,Box

# Crear un cajero y cliente
cashier = Cashier("12345678A", "Ana", 30, "morning", 1200)
customer = Customer("87654321B", "Juan", 25, 'juan@gmail.com', 46004)

# Crear la orden
order_1 = Order(cashier, customer)

# Crear productos
burger = Hamburger("HAM1", "Chesee",5.99,)
drink = Drink("S1","Coke", 2.50)
happy_meal = HappyMeal("HM1","Kids Menu", 6.99,)

# Añadir productos a la orden
order_1.add(burger)
order_1.add(drink)
order_1.add(happy_meal)

# Mostrar
order_1.show()

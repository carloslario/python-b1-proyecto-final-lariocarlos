from users import *
from products import *

class Order:
  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
    #Write your code here
    #se añade cada producto a la lista
    self.products.append(product)
    pass

  def calculateTotal(self) -> float:
    #Write your code here
    #Se calcula la factura total de los productos
    suma = 0
    for producto in self.products:
      suma += producto.price
    return suma
  
  def show(self):    
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Total price : {self.calculateTotal()}")

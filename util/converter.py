from abc import ABC, abstractmethod
#Write your code here
import pandas as pd
from users.user import User , Customer , Cashier
from products.product import Hamburger, HappyMeal, Drink, Soda
from util.file_manager import CSVFileManager

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):    
    #Write your code here
    cashiers = []
    
    for row in dataFrame.itertuples(index=False, name=None):
        cashier = Cashier(row[0], row[1], row[2], row[3], row[4])
        cashiers.append(cashier)
    return cashiers

class CustomerConverter(Converter):
  #Write your code here
  def convert(self,dataFrame):  
    customers = []
    
    for row in dataFrame.itertuples(index=False):
      customer = Customer(row.name, row.dni, row.age, row.email, row.postalcode)
      customers.append(customer)
    return customers

class ProductConverter(Converter):
  #Write your code here

 def convert(self, dataFrame: pd.DataFrame) -> list: 
  product = [] 

  #Para tipo bebidas 
  if "B" in dataFrame["id"]: 
   for row in dataFrame.itertuples(index=False): 
     product = Drink(row.id, row.name, row.price) 

 #Para tipo hamburgesas 
  if "H" in dataFrame["id"]: 
   for row in dataFrame.itertuples(index=False): 
    product = Hamburger(row.id, row.name, row.price) 

#Para tipo sodas 
  if "G" in dataFrame["id"]: 
   for row in dataFrame.itertuples(index=False): 
    product = Soda(row.id, row.name, row.price)

 #Para tipo Happy Meal 
  if "HM" in dataFrame["id"]: 
   for row in dataFrame.itertuples(index=False): 
    product = HappyMeal(row.id, row.name, row.price) 

  return product
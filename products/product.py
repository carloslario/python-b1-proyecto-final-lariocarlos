from abc import ABC, abstractmethod
#Write your code here
from food_package import *

class Product(ABC):
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self):
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        pass
    @abstractmethod
    def foodPackage(self)->FoodPackage:
        pass  

class Hamburger(Product):
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburguesa"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
class Soda(Product):
    #Write your code here
    #Aqui defino que los productos tipo Soda se sirven en formato botella (Bottle)
    #Por que lo que asigno la clase Bottle()
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Soda"
    def foodPackage(self) -> FoodPackage:
        return Bottle()

class Drink(Product):
    #Write your code here
    #Aqui defino que los productos tipo Bebida se sirven en formato vaso (Glass)
    #Por que lo que asigno la clase Bottle()
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Drink"
    def foodPackage(self) -> FoodPackage:
        return Glass()

class HappyMeal(Product):
    #Write your code here
    #Aqui defino que los productos tipo HappyMeal se sirven en formato box (caja)
    #Por que lo que asigno la clase Box()
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Box"
    def foodPackage(self) -> FoodPackage:
        return Box()
#Write your code here
from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
  #Write your code here
  #al ser un metodo abstracto, las clases hijas deben implementar el metodo tambien
  def pack(self):
     return "Food Wrap Paper"
  
  def material(self):
     return "Aluminium"

class Bottle(FoodPackage):  
  #Write your code here
  #el tipo de paquete es bottle (botella)
  def pack(self):
    return "Bottle"
  
  #el material del paquete es plastic
  def material(self):
     return "Plastic"
      
class Glass(FoodPackage):  
  #Write your code here
  #el tipo de paquete es Glass (vaso)
  def pack(self):
    return "Glass"
  
  #el material del paquete es cardboard (carton)
  def material(self):
     return "Cardboard"

class Box(FoodPackage):  
  #Write your code here
  #el tipo de paquete es box (caja)
  def pack(self):
    return "Box"
  
  #el material del paquete es Polystyrene (poliestireno)
  def material(self):
     return "Polystyrene"
import pandas as pd

class CSVFileManager:
  def __init__(self,path: str):
    self.path = path
  def read(self) -> str:
    return pd.read_csv(self.path)  
  def write(self,dataFrame):
    #La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. 
    # Esta es una función opcional, se deja al estudiante la implementación.
    pass

dt = CSVFileManager("data/happyMeal.csv")
dt_r = dt.read()
print(dt_r['id'])
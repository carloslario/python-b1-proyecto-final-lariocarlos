"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
from users import *
from util import *
from products import *
from orders.order import Order
from time import sleep

class PrepareOrder:
 #Write your code here
 def __init__(self):
    self.cashiersDF = None
    self.customersDF = None
    self.cashiers = []
    self.customers = []
   
 def read_csv(self):
        self.cashiersDF = CSVFileManager("data/cashiers.csv").read()
        self.customersDF = CSVFileManager("data/customers.csv").read()
        self.drinksDF = CSVFileManager("data/drinks.csv").read()
        self.hamburgersDF = CSVFileManager("data/hamburgers.csv").read()
        self.happyMealDF = CSVFileManager("data/happyMeal.csv").read()
        self.sodasDF = CSVFileManager("data/sodas.csv").read()

        #Se unen todos los productos bajo el mismo dataframe
        self.productsDF = pd.concat(
    [
        self.drinksDF,
        self.hamburgersDF,
        self.happyMealDF,
        self.sodasDF
    ],
    ignore_index=True
)
        pass

 def convertDataFrames(self):
        self.cashiers = CashierConverter().convert(self.cashiersDF)
        self.customers = CustomerConverter().convert(self.customersDF)

 def menu_products(self):
      #Metodo para mostrar el menu completo
      print("MENU DRINKS")
      print(self.drinksDF)
      print("\n------------------------------------------------------")
      print("MENU HAMBURGERS")
      print(self.hamburgersDF)
      print("\n------------------------------------------------------")
      print("MENU HAPPYMEAL")
      print(self.happyMealDF)
      print("\n------------------------------------------------------")
      print("MENU SODAS")
      print(self.sodasDF)
      print("\n------------------------------------------------------")
      pass


 def main(self):
       self.read_csv()
       self.convertDataFrames()

       #1. Se selecciona el cajero
       print(self.cashiersDF)
       print("\n------------------------------------------------------")
       sleep(0.5)
       DNI_cajero = input("Introduce el DNI del cajero: ")
       sleep(0.5)
       while DNI_cajero not in self.cashiersDF["dni"].astype(str).values:
             print(self.cashiersDF)
             DNI_cajero = str(input("DNI invalido. Introduce el DNI del cajero: "))
       self.dt_filtrado = self.cashiersDF[self.cashiersDF["dni"].astype(str) == DNI_cajero]

       cajero_lista = CashierConverter().convert(self.dt_filtrado)
       cajero_obj = cajero_lista[0]
       print(cajero_obj.describe())

       #2. Se selecciona el cliente
       print(self.customersDF)
       print("\n------------------------------------------------------")
       sleep(0.5)
       DNI_cliente = input("Introduce el DNI del cliente: ")
       sleep(0.5)
       while DNI_cliente not in self.customersDF["dni"].astype(str).values:
             print(self.customersDF)
             DNI_cliente = str(input("DNI invalido. Introduce el DNI del cliente: "))
       self.dt_filtrado = self.customersDF[self.customersDF["dni"].astype(str) == DNI_cliente]

       cliente_lista = CustomerConverter().convert(self.dt_filtrado)
       customer_obj = cliente_lista[0]
       print(customer_obj.describe())

       #3. Se crea la orden
       self.menu_products()
       self.order = Order(cajero_obj,customer_obj)
       add_product = True
       lista_pedido = []
       while add_product:
            prod_id = input("Introduce ID de producto: ")

            while prod_id not in self.productsDF["id"].astype(str).values:

                prod_id = str(input("ID de producto invalido. Introduce el Id del producto: "))

            lista_pedido.append(prod_id)
            print(f"Producto {prod_id} añadido.\n")
            add_product = input("Añadir otro producto? (1: Si/ Otro: No): ")

            if add_product.lower() != "1":
                 add_product = False
       
       #4. Se muestra el pedido completo
       print("                         PEDIDO")
       print("------------------------------------------------------")
       for item in lista_pedido:
            print(item)
       print("------------------------------------------------------")

       #5. Se calcula el pedido completo
       self.lista_pedido_obj = []
       print(lista_pedido)

       for item in lista_pedido:
            prod_filtrado = self.productsDF[self.productsDF["id"].astype(str) == item]  # DataFrame filtrado
            prod_instance = ProductConverter().convert(prod_filtrado)  # UNA instancia
            #print(prod_instance.id)
            self.order.add(prod_instance)
            self.lista_pedido_obj.append(prod_instance)
            
       self.order.show()
       
PrepareOrder().main()
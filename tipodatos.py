print("Clases V2 Eliseo Nava")
#Zona de clase
class Datos:
    #El constructor
    def __init__(self, estatura,peso):
        self.estatura=estatura
        self.peso=peso 
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso: {self.peso} Kg")
    def mi_lista(self):
        Carros=["Dodge Challenger RT Shaker","Chevrolet Camino SS","Ford Pinto"]
        print(Carros)
        for car in Carros:
            print(car)
    def mi_tupla(self):
        Frutas=("Banana","Manzana","Uva")
        print(Frutas)
        for fruit in Frutas:
            print(fruit)
    def mi_set(self):
        Animales={"Zorro","Perro","Gato"}
        print(Animales)
        for Animal in Animales:
            print(Animal)
    def mi_dic(self):
        Diccionario = {
            "Marca:": "Volkswagen",
            "Modelo:": "Golf R",
            "Año:": 2016
            }
        for dick, di in Diccionario.items():
            print(dick,di)

#creacion de objeto info
info=Datos(1.75,70)

#utilizando el obj.
info.mostrar_datos()
print("Lista de mis carros favoritos")
info.mi_lista()
print("Tupla de frutas")
info.mi_tupla()
print("Sets de animales")
info.mi_set()
print("Diccionario de un carro")
info.mi_dic()
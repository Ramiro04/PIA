from tkinter import SEPARATOR
import numpy as np
import random
SEPARATOR = ("*" * 20) + "\n"

#Comprobacion de que un array de numpy y una lista no poseen el mismo comportamiento:
#Una lista puede contener elementos de diferentes tipo de dato 
#en una array de numpy todos los elementos son del mismo tipo de dato

lista = [10, "abc", 20]
print(lista)
print([type(elemento) for elemento in lista])
print(SEPARATOR)

#si se le proporciona un elemento de un tipo de dato difernte, numpy 
#integrar los valores a un tipo "neutro" que los pueda abarcar (usualmente)
arreglo = np.array([10,"abc", 20])
print(arreglo)
print([type(elemento) for elemento in arreglo])
print(SEPARATOR)

#una lista no ofrece operaciones de algebra matricial, por ejemplo:
#la multiplicacion de un array o matriz por un esclar, o por una
lista = [10, 15, 20, 25]
print(lista)
print(lista * 2)
print(SEPARATOR)

arreglo = np.array([10, 15, 20, 25])
print(arreglo)
print(arreglo * 2)
print(SEPARATOR)

matrizA = np.array([[random.randraange(300) for valor in range(10)] for valor in range(5)])
matrizB = np.array([[random.randraange(300) for valor in range(10)] for valor in range(5)])

print(f"matriz A\n{matrizA}")
print("\nX\n")
print(f"matriz B\n{matrizB}")
print("\n=\n")
print(matrizA * matrizB)

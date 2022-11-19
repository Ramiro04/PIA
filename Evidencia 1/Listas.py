from tkinter import SEPARATOR


SEPARATOR = ("*" * 20) + "\n"

#Creacion de listas 
#Lista vacia
lista_vacia = list()
otra_lista_vacia = []
#Lista con elementos iniciales
lista_uno = [1, 2, 3, 4]
print(lista_uno)
print(SEPARATOR)
pass

#Agregar elementos a listas existentes
lista_uno.append(5)
print(lista_uno)
lista_uno.append((6, 7)) #una lista puede ser un elemento de otra lista 
print(lista_uno)
print(SEPARATOR)
pass
#Remover elementos de una lista 
lista_uno.remove((6, 7))
print(lista_uno)
print(SEPARATOR)
pass

#Ordenar elements de una lista
#sort()
lista_original1 = [3, 4, 2]
print(lista_original1)
lista_original1.sort()
print(lista_original1)
pass

#sorted
lista_original2 = [23, 10, 30, 5]
lista_ordenada = sorted(lista_original2)
print(f"lista original = {lista_original2}, y la version ordenada es {lista_ordenada}")
print(SEPARATOR)
pass

#comprension de listas
print(f"lista original = {lista_uno}")

#SIN comprension de listas
lista_uno_al_doble = []
for valor in lista_uno:
    lista_uno_al_doble.append(valor*2)
print(f"lista resultante, cada elemento al doble = {lista_uno_al_doble}")
pass

#CON comprension de listas
lista_uno_al_doble = [valor * 2 for valor in lista_uno]
print(f"Mismo resultado, pero con comprension de listas = {lista_uno_al_doble}")
pass

#Comprension de listas con condicion
Listas_valores_pares = [valor for valor in lista_uno if (valor % 2 == 0)]
print(f"solamente se agregaron los elementos con valor par: {Listas_valores_pares}")
pass


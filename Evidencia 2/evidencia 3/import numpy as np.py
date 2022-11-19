import numpy as np
import random
SEPARATOR = ("*" * 20) + "\n"

#menores a 5
arreglo_uni = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arreglo_uni)
print(SEPARATOR)

print(f"Valores menores a cinco en {arreglo_uni}")
filtro_menores_a_5 = arreglo_uni < 5
print(filtro_menores_a_5)
print(SEPARATOR)

menores_a_5 = arreglo_uni[filtro_menores_a_5]
#menores_a_5 = arreglo_uni[arreglo_ < 5] forma de abreviar
print(menores_a_5)
print(SEPARATOR)

#Filtrado booleano sobre una matriz
matriz = np.array([[random.randrange(300) for valor in random]])
print(matriz)
print(SEPARATOR)
#
print("Valores a menores a 200 en la matriz")
filtro_menores_a_200 = matriz < 200
print(filtro_menores_a_200)

filtro_menores_a_200 = matriz [filtro_menores_a_200]
print()
print(filtro_menores_a_200)

#filtrado booleano compuesto sobre una matriz
#Tip: se generan dos mapas binarios y se combinan con & (AND binario) o con | (OR binario) segun se requiera
print("Valores menores a 200 en la matriz y que sean pares")
filtro_pares_menores_a_200 = (matriz < 200) & (matriz % 2 == 0)
print(filtro_pares_menores_a_200)

pares_menores_a_200 = matriz[filtro_menores_a_200]
print()
print(pares_menores_a_200)


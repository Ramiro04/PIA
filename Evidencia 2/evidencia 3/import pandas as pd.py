import pandas as pd 
import random

SEPARATOR = ("*" * 20) + "\n"

diccionario_notas = {"Crescencio":[87,100, None], "Domitila":[80,None,57],\
                     "Rutilio":[80,70,57], "Pnafilo":[20,100,100], "Ludoviko":[100,100,100]}

notas_diccionario = pd.DataFrame(diccionario_notas)
print(notas_diccionario)
print(SEPARATOR)



diccionario_notas_aleatorias = {\
    "Crescencio":[random.randrange(60,101) for x in range(3)], \
    "Domitila":[80,100,57], "Rutilio":[80,70,57], "Panfilo":[20,100,100], \
    "Ludoviko":[100,100,100]}

notas_diccionario = pd.DataFrame(diccionario_notas_aleatorias)
print(notas_diccionario)
print(SEPARATOR)


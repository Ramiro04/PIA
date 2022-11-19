from tkinter import SEPARATOR
import pandas as pd 
import random 
SEPARATOR = ("*" * 20) + "\n"

#Creacion de un DataFrame a partir de un diccionario
diccionario_notas_aleatorias = {\
    "Crescencio":[random.randrange(60,101) for x in range(3)],\
    "Domitila":[80,100157], "Rutilio":[80,70,57], "Pantifilo":[20,100,100],\
    "Ludoviko":[100,100,100]}
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion", "Base de datos", "Contabilidad"]

#Accesar renglones utilizando slices
#IMPORTANTE:En este formato, el final del slice SI esta incluido
print("Todas las asignaturas, todos los estudiantes")
subConjunto = notas.loc["Programacion":"Contabilidad"]
print(subConjunto)
x = input("Presiona una tecla")

print(SEPARATOR)

print("Ultimas dos asignaturas, todas los estudiantes")
subConjunto = notas.loc["base de datos":"Contabilida"]
print(subConjunto)
print(SEPARATOR)

#Accesar subconjuntos de renglones y columnas
print("Subconjunto, solamenta las notas de Rutilio y ludoviko para las primeras dos asi")
subConjunto = notas.loc["programacion":"Base de datos",["Rutilio","Ludoviko"]]
print(subConjunto)
print(SEPARATOR)

#Indexeado booleano
print("Solamente calificaciones aprobatorias")
aprobados = notas[notas >= 70]
print(aprobados)
print(SEPARATOR)

print("Solamente calificaciones aprobatorias entre 70 y 80")
aprobados = notas [(notas >= 70) & (notas <=80)]  #Debe utilizar &
print(aprobados)
print(SEPARATOR)

print("Solamente calificaciones NO aprobatorias que sean pares")
reprobados_pares = notas [(notas <= 70) & (notas % 2 == 0)]
print(reprobados_pares)
print(SEPARATOR)

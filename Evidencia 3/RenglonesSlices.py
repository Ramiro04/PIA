import pandas as pd 
import random 
SEPPARADOR = ("*" * 20) + "\n"

#Creacion de una DataFrame a partir de una direccion 
diccionario_notas_aleatorias = { \ 
    "Cresencio": [random.randrange(60,101) for x in range(3)], \
    "Domitila": [80,100,57], "Rutilio": [80,70,57], "Panfilo": [20,100,100], \
    "Ludoviko": [100,100,100] }  
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion", "Base de datos", "Contabilidad"]

#Accesar renglones utilizando slices
#IMPORTANTE: En este formato, el final del slice SI esta incluido
print("Todas las asignaturas, todos los estudiantes")
subConjunto = notas.loc["Programacion": "contabilidad"]
print(subConjunto)
x = input("Precencia una tecla")


print(SEPPARADOR)

print("Unltimas dos  asignaturas, todos los estudiantes")
subConjunto = notas.loc["Base de datos": "Contabilidad"]
print(subConjunto)
print(SEPPARADOR)

#Accesar subConjuntos de renglones y columnas
print("subConjunto, solamente las notas de Rutilio y Ludoviko para las primeras dos asignaturas")
subConjunto = notas.loc["Programacion": "Base de datos", ["Rutilio","Ludoviko"]]
print(subConjunto)
print(SEPPARADOR)

#Indexado booleano
print("Solamente calificaciones aprobatorias")
aprobados = notas[notas>= 70]
print(aprobados)
print(SEPPARADOR)

print("Solamente calificaciones aprobatorias entre 70 y 80")
aprobados = notas[(notas >=  70) & (notas <= 80)]  #DEBE utilizarse &
print(aprobados)
print(SEPPARADOR)

print("Solamente calificaciones NO aprobatorias que sean pares") 
reprobados_pares = notas[(notas <= 70) & (notas % 2 == 0)]
print(reprobados_pares)
print(SEPPARADOR)

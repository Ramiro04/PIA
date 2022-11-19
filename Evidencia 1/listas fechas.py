import datetime
SEPARATOR = "*" * 30

def calcula_edad(fecha_nac):

lista_fechas = []
for elemento in range(3):
    fecha_capturada = input("dime una fecha (dd/mm/aaaa): \n")
    fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d%m/%y").date()
    lista_fechas.append(fecha_procesada)

print(SEPARATOR)

edades = list(map(calcula_edad, lista_fechas))

for edad in edades:
    print(edad)
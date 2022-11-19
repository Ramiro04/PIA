import datetime
import time
from tkinter import SEPARATOR
SEPARATOR = ("*" * 20) + "\n"

#Creacion de una hora esoecifica 
hora = datetime.time (10, 20, 30)
print(f"el tipo de objeto de hora es {type(hora)}")
print(f"la hora es {hora}")
print(f"la hora de {hora} es {hora.hour}")      #limitado 0..23
print(f"el minuto de {hora} es {hora.minute}") #limitado 0..59
print(f"el segundo de {hora} es {hora.second}")#limitado 0..59
print(f"el microsegundo de {hora} es {hora.microsecond}") #limitado 0..99
print (SEPARATOR * 2)

#determina la fecha del sistema 
fecha_actual = datetime.date.today()
print(f"el tipo de objeto de la fecha es {fecha_actual}")
print(f"la fecha actual es {fecha_actual}")
print(f"el año actual es {fecha_actual.year}")
print(f"el mes actual es {fecha_actual.month}")
print(f"el dia actual es {fecha_actual.day}")
print(SEPARATOR * 2)

#convertir un string a fecha 
cant_capturada = int(input("dime la cantidd de dia a adelantar:\n"))
nueva_fecha = fecha_procesada + datetime.timedelta(days=+cant_dias)
print(f"la jueva fecha es {nueva_fecha}")
print(SEPARATOR)

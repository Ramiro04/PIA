import math 
SEPARADOR = ("*" * 20) + "\n"
'''
Ejemplo

'''

valorflotante = float(input("introduce un valor con fraccion decimal:\n"))
print(f"El siguiente entero hacia arriba de {valorflotante} es {math.ceil(valorflotante)}")
print(SEPARADOR)
print(f"El siguiente entero hacia abajo de {valorflotante} es {math.floor(valorflotante)}")
print(SEPARADOR)
print(f"La parte entera truncada de {valorflotante} es {math.trunc(valorflotante)}") #Equivalente a floor() para negativos porque se mueve hacia el 0
print(SEPARADOR * 2)
pass
valorNumerico =int(input("dame un valor entero>\n"))
print(f"la raiz cuadrada de {valorNumerico} es igual a {math.sqrt(valorNumerico)}")
print(SEPARADOR)
print(f"El factorial de {valorNumerico} es igual a {math.factorial(valorNumerico)}")
potencia = int(input("dame un valor entero:\n"))
print(f"El resultado de elevar {valorNumerico} a la {potencia} potencia es igual a {math.pow(valorNumerico,potencia)}")
print(SEPARADOR * 2)
pass


print(f"el valor de Pi es {matj.pi}")

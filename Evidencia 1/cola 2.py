'''
Demostracion de implementacion de pilas utilizando listas y con deques 

'''
import collections
SEPARADOR = ("*" * 20) + "\n"

pila_con_listas = list()
for i in range(5):
    pila_con_listas.append(input("Dime el nombre a agregar: "))

#Sacar elementos de la pila
while pila_con_listas:
    print(pila_con_listas.pop())
print(SEPARADOR)

pila_deque = collections.deque()
for i in range(5):
    pila_deque.append(input("dime el nombre a agregar: "))

#Sacar elementos de la pila
while pila_deque:
    print(pila_deque.pop())
pass       

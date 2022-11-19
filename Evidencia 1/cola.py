'''''
Implementacion de colas mediante listas y deque () 
Demuestra las diferencias en la forma de implementacion 

'''''
SEPARADOR = ("*" * 20) + "/n"

cola = list()  #colautilizando una lista 

for cantidad in range(5):
    nuevo = input("nombre del recien llegado:")
    cola.append(nuevo)

print(f"Se agregaron {len(cola)}, elementos")
for elemento in cola:
    print(elemento)
print(SEPARADOR)
pass #hacer notar que los elementos permanecen en la cola

print("Procedemos a retirarlos de la cola")
while cola:
    print(cola.pop(0))
pass  #verificar qe las estructuras se encuentra vacia    


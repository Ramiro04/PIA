from tkinter import SEPARATOR
from tkinter.ttk import Separator
import numpy as np
SEPARATOR = ("*" * 20) + "\n"

#mayores a 3 
arreglo_uni = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arreglo_uni)
print(SEPARATOR)

menores_a_5 = arreglo_uni[arreglo_uni< 5]
print(menores_a_5)
print(SEPARATOR)

mayores_a_5 = arreglo_uni[arreglo_uni > 5]
print(mayores_a_5)
pass

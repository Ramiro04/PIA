import pandas as pd 
SPEPARADOR = ("*"  * 20) + "\n"

notas = pd.read_csv("notas.csv", index_col=0)

print(notas)
print(SPEPARADOR)

#3.7.1 Listas dentro de listas
#las listas pueden constar de escalares (es decir, números) y elementos de una estructura mucho más compleja (ya has visto ejemplos como cadenas, booleanos o incluso otras listas en las lecciones del Resumen de la Sección anterior). Veamos más de cerca el caso en el que los elementos de una lista son listas.
from sre_parse import WHITESPACE


row = []

for i in range(8):
    row.append(WHITESPACE)


#3.7.2 Arreglos de dos dimensiones

board = []

for i in range(8):
    row = [EMPTY for i in range(8)] # type: ignore
    board.append(row)

#3.7.3 Naturaleza multidimensional de las listas: aplicaciones avanzadas
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Temperatura promedio al mediodía:", average)



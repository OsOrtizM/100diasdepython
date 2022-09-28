"""
        Bienvenido al día 72 de #100diasdepython
                El reto de hoy es:
Utiliza itertools para obtener la cantidad de veces que
        se repite cada número de la lista
        [0, 1, 1, 2, 3, 2, 4, 5, 5, 8, 4]
Imprime el resultado en un diccionario con el formato
        {numero:cantidad de repeticiones}
"""
import itertools

diccionario = dict()
numeros = [0, 1, 1, 2, 3, 2, 4, 5, 5, 8, 4]
for num, group in itertools.groupby(sorted(numeros)):
    acumulador = 0
    for x in group:
        acumulador += 1
    diccionario[num] = acumulador

print(diccionario)

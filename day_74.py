"""
Bienvenido al día 74 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener el producto
    cartesiano de las siguientes lista
            [1, 3, 5] y [2, 4, 6]
Imprime el resultado en una lista de tuplas
"""
import itertools

lista_1, lista_2 = [1, 3, 5], [2, 4, 6]
prod_cartesiano = list(itertools.product(lista_1, lista_2))
print(prod_cartesiano)

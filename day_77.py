"""
Bienvenido al día 77 de #100diasdepython
            El reto de hoy es:
    Utiliza itertools para obtener los
    multiplos de 5 de la siguiente lista
        [1, 5, 10, 23, 3, 555, 11, 10]
    Imprime el resultado en una lista
"""
import itertools

lista = [1, 5, 10, 23, 3, 555, 11, 10]
multiplos_5 = list(itertools.filterfalse(lambda x: (x % 5) != 0, lista))
print(multiplos_5)

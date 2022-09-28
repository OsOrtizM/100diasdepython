"""
Bienvenido al día 92 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use yield y genere la
 siguiente serie [1, 2, 3, 2, 1, 2, 3, 2, 1]
        Imprime el resultado en una Lista
"""


def serie():
    for n in [1, 2, 3, 2, 1, 2, 3, 2, 1]:
        yield n


numbers = serie()

lista = [i for i in numbers]
print(lista)

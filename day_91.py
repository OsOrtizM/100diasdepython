"""
Bienvenido al día 91 de #100diasdepython
            El reto de hoy es:
    Crea una funcion que devuelva los cuadrados
de los primeros 10 numeros enteros iniciando en 1
                utilizando yields
        Imprime el resultado en una Lista
"""


def first10numbers():
    for n in range(1, 11):
        yield n ** 2


numbers = first10numbers()

lista = [i for i in numbers]
print(lista)


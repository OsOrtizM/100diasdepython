"""
    Bienvenido al día 93 de #100diasdepython
                El reto de hoy es:
Crea una funcion que use yield y genere los primeros
        10 numeros de la serie de Fibonacci
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        Imprime el resultado en una Lista
"""


def fibonacci(limit):
    n1, n2 = 0, 1
    for _ in range(limit):
        n1, n2 = n2, n1 + n2
        yield n1


fibos = fibonacci(10)

lista = [f for f in fibos]
print(lista)

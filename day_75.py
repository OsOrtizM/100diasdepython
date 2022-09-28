"""
    Bienvenido al día 75 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para obtener el mensaje secreto
    en la siguiente cadena "P1y2t3h4o5n6!7"
    Imprime el resultado en una cadena
            Te dejamos una pista:
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
"""
import itertools

cadena = "P1y2t3h4o5n6!7"
pista = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
mensaje_secreto = ''.join(list(itertools.compress(cadena, pista)))
print(mensaje_secreto)

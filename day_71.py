"""
        Bienvenido al día 71 de #100diasdepython
                El reto de hoy es:
    Utiliza itertools para generar una serie
    de sumas acumuladas con los números de la
    siguiente lista  [0, 1, 1, 2, 3, 5, 8]
            Imprime el resultado
"""
import itertools

numeros = [0, 1, 1, 2, 3, 5, 8]
acumulados = list(itertools.accumulate(numeros))
print(acumulados)

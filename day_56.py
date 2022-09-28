"""
    Bienvenido al dia 56 de #100diasdepython
            El reto de hoy es:
    Utiliza la funcion lambda para encontrar la raiz
cuadrada de esta lista de numeros [49, 4, 36, 16, 25]
    Imprime el resultado en nueva lista
"""
import math

numeros = [49, 4, 36, 16, 25]
nueva_lista = list(map(lambda x: math.sqrt(x), numeros))
print(nueva_lista)

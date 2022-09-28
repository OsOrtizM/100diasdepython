"""
    Bienvenido al dia 50 de #100diasdepython
            El reto de hoy es:
    Genera 5 numeros enteros de forma aleatoria
            Almacenalos en una lista
        Sumalos e imprime el resultado
"""
import random

aleatorios = [random.randint(0, 10) for x in range(5)]

print(sum(aleatorios))
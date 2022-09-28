"""
    Bienvenido al dia 48 de #100diasdepython
            El reto de hoy es:
    Con un rango de 5 numeros crea una lista
    que refleje con valores booleanos cuales
        son pares e imprime el resultado
"""
numeros = [(x % 2 == 0) for x in range(5)]
print(numeros)

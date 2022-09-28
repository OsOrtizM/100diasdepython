"""
    Bienvenido al día 95 de #100diasdepython
                El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
    para recibir N-numeros y determine cual es
el mayor y el menor y los devuelva en un diccionario
en el siguiente formato {'mayor': 5, 'menor': -10}
                Imprime el resultado
"""


def mayor_menor(*numeros):
    return {'mayor': max(numeros), 'menor': min(numeros)}


print(mayor_menor(2, 3, 4, 5, -10, -9))

"""
    Bienvenido al dia 51 de #100diasdepython
            El reto de hoy es:
Crea una funcion que calcule el volumen de un cilindro
    Los parametros de entrada son base y altura
    El valor de salida volumen del cilindro
Ejecuta al funcion para el caso base= 5, altura= 7
            Imprime el resultado
"""
import math


def volumen_cilindro(base, altura):
    return math.pi * math.pow(base / 2, 2) * altura


print(volumen_cilindro(5, 7))

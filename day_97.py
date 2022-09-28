"""
Bienvenido al día 97 de #100diasdepython
            El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
de tipo Keyword para recibir los 3 lados de un
        triangulo y calcule su perimetro
Imprime el resultado en un numero de punto flotante
"""


def perimetro_triangulo(**data):
    return sum(data.values())


print(perimetro_triangulo(lado1=3, lado2=4, lado3=6))

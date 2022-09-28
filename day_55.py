"""
    Bienvenido al dia 55 de #100diasdepython
            El reto de hoy es:
    Crea una funcion recursiva para hacer una
            cuenta regresiva a 0
La funcion tiene como parametro de entrada un numero
    Ejecuta la funcion para el numero 5
Imprime el valor de la cuenta en cada iteracion
"""


def countdown_to_0(num):
    print(num)
    if num:
        countdown_to_0(num - 1)


countdown_to_0(5)

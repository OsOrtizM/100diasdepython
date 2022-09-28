"""
    Bienvenido al dia 53 de #100diasdepython
            El reto de hoy es:
    Crea una funcion que reciba una lista de
numeros y devuelva una lista de los numeros al cuadrado
    Ejecuta la funcion para la lista [2, 3, 5, 7, 11]
                Imprime el resultado
"""


def list_to_power_of_two(list_input):
    list_output = list(map(lambda x: x * x, list_input))
    return list_output


print(list_to_power_of_two([2, 3, 5, 7, 11]))

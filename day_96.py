"""
        Bienvenido al día 96 de #100diasdepython
                    El reto de hoy es:
Crea una funcion que use argumentos arbitrarios de tipo
Keyword para recibir nombre, apellido y edad y devuelva
estos argumentos en un diccionario en el siguiente formato
    {'nombre': "Pepito", 'apellido': "Perez", 'edad': 35}
                Imprime el resultado
"""


def mayor_menor(**data):
    return {'nombre': data['nombre'], 'apellido': data['apellido'], 'edad': data['edad']}


print(mayor_menor(nombre='Pepito', apellido='Perez', edad=35))

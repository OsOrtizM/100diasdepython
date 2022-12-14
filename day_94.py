"""
    Bienvenido al día 94 de #100diasdepython
                El reto de hoy es:
Crea una funcion que use argumentos arbitrarios
    para recibir N-cadenas de nombres y
        devuelva una lista de N-saludos
    ejemplo de salida ['Hola Katy', 'Hola Ariel']
        Imprime el resultado en una Lista
"""


def saludar(*nombres):
    return ['Hola ' + n for n in nombres]


persona_1, persona_2 = 'Katy', 'Ariel'
saludos = saludar(persona_1, persona_2)
print(saludos)

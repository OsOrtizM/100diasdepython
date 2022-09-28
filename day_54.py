"""
    Bienvenido al dia 54 de #100diasdepython
            El reto de hoy es:
Crea una funcion que reciba una lista de cadenas y
    devuelva un diccionario con la cantidad
            de vovales de cada cadena
Ejempla de entrada: ['Python', 'es', 'cool']
Ejemplo de salida: {'Python': 1, 'es': 1, 'cool': 2}
                Imprime el resultado
"""


def list_to_count_vowels_to_dictionary(list_input):
    dicc_output = {}
    for item in list_input:
        count_vowel = 0
        for char in item:
            if char in 'AEIOUaeiou':
                count_vowel += 1
        dicc_output[item] = count_vowel
    return dicc_output


print(list_to_count_vowels_to_dictionary(['Python', 'es', 'cool']))

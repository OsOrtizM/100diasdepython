"""
    Bienvenido al dia 63 de #100diasdepython
            El reto de hoy es:
Utiliza RegEx para validar que las cadenas solo
        contengan caracteres alfanumericos
["Python3.10", "Python3", "ProgramandoAndo", "jun2022",
        "#100diasdecodigo", "Felicidades!"]
    Imprime una lista con las cadenas validas
"""
import re

lista = ["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
regex = re.compile(r'\w+')
lista_validas = list(filter(lambda x: regex.fullmatch(x) is not None, lista))

print(lista_validas)

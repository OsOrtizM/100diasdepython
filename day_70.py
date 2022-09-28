"""
        Bienvenido al día 70 de #100diasdepython
                El reto de hoy es:
    Utiliza RegEx para extraer todas las palabras que
    contengan el menos una 'a' en la siguiente cadena
        "Llevas programando 70 dias seguidos"
    Imprime una lista con las palabras extraidas
"""
import re

cadena = "Llevas programando 70 dias seguidos"
regex = re.compile(r'\w*a+\w*')
palabras = regex.findall(cadena)

print(palabras)

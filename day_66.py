"""
    Bienvenido al día 66 de #100diasdepython
            El reto de hoy es:
    Utiliza RegEx para eliminar los caracteres que
    no sean alfanumericos en las cadenas de la lista
["Python3.10", "Python3", "ProgramandoAndo", "jun2022",
        "#100diasdecodigo", "Felicidades!"]
    Imprime una lista con las cadenas limpias
"""
import re

cadenas = ["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
cadenas_limpias = []
regex = re.compile(r'[^A-Za-z\d]+')
for cadena in cadenas:
    cadena_limpia = re.sub(regex, '', cadena)
    cadenas_limpias.append(cadena_limpia)

print(cadenas_limpias)

"""
        Bienvenido al día 69 de #100diasdepython
                El reto de hoy es:
Utiliza RegEx para extraer todas las 'a' seguidas de
        una o mas 'b's de la siguiente cadena
        "abholaaaaabaaabbpythonistaaaaaabbbbb"
Imprime una lista con las subcadenas extraidas
"""
import re

cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"
regex = re.compile(r'a+b')
subcadenas = regex.findall(cadena)

print(subcadenas)

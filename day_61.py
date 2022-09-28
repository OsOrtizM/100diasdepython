"""
    Bienvenido al dia 61 de #100diasdepython
            El reto de hoy es:
    Utiliza RegEx para validar que las cadenas de
        la lista sean totalmente numericas
["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
        Imprime una lista con las cadenas numericas
"""
import re

lista = ["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
regex = re.compile(r'\d+')
lista_numericos = list(filter(lambda x: regex.fullmatch(x) is not None, lista))

print(lista_numericos)

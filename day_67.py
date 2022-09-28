"""
    Bienvenido al día 67 de #100diasdepython
            El reto de hoy es:
Utiliza RegEx para cambiar el formato de las fechas
de YYYYMMDD a YYYY-MM-DD de las fechas de la lista
["20221205", "19930612", "20050126", "20211008"]
        Imprime una lista con las fechas
"""
import re

fechas = ["20221205", "19930612", "20050126", "20211008"]
fechas_formateadas = []
regex = re.compile(r'(\d{4})(\d{2})(\d{2})')
for fecha in fechas:
    captura = regex.search(fecha)
    if captura:
        grupos = captura.group(1, 2, 3)
        fechas_formateadas.append(grupos[0] + '-' + grupos[1] + '-' + grupos[2])

print(fechas_formateadas)

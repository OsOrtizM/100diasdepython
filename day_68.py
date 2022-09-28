"""
    Bienvenido al día 68 de #100diasdepython
            El reto de hoy es:
Utiliza RegEx para cambiar el formato de las fechas
de YYYY-MM-DD a DDMMYYYY de las fechas de la lista
["2022-12-05", "1993-06-12", "2005-01-26", "2021-10-08"]
Imprime una lista con las fechas con el nuevo formato
"""
import re

fechas = ["2022-12-05", "1993-06-12", "2005-01-26", "2021-10-08"]
fechas_formateadas = []
regex = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
for fecha in fechas:
    captura = regex.search(fecha)
    if captura:
        grupos = captura.group(1, 2, 3)
        fechas_formateadas.append(grupos[2] + grupos[1] + grupos[0])

print(fechas_formateadas)

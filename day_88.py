"""
Bienvenido al día 88 de #100diasdepython
            El reto de hoy es:
Utiliza calendar para imprimir la cantidad
    de semanas en cada mes del año 2022
"""
from calendar import Calendar
import collections

anio = 2022
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
         'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
semanasXmes = dict()
cal = Calendar()

semanas = [meses[mes] for mes in range(12) for semana in cal.monthdayscalendar(anio, mes+1) if semana.count(0) < 4]

print(dict(collections.Counter(semanas)))

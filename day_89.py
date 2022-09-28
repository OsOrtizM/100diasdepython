"""
Bienvenido al día 89 de #100diasdepython
            El reto de hoy es:
Utiliza calendar para obtener los dias lunes
        del mes Julio del año 2022
    Imprime el resultado en una lista
"""
import calendar

julio = calendar.monthcalendar(2022, 7)
lunes = list(map(lambda x: x[0], filter(lambda x: x[0] > 0, julio)))
print(lunes)

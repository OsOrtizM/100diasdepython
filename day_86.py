"""
Bienvenido al día 86 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para calcular la cantidad
de segundos que han pasado desde el inicio
    del reto considerando solo la fecha
Considera que el reto inicio el "20/04/2022"
            Imprime el resultado
"""
import datetime as dt

inicio = dt.datetime.strptime("20/04/2022", '%d/%m/%Y')
hoy = dt.datetime.strptime("14/07/2022", '%d/%m/%Y')
print((hoy - inicio).total_seconds())

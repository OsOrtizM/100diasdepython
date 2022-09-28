"""
Bienvenido al día 82 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para imprimir la fecha y hora
actual en el formato "10 July 2022, 12:12:12 AM"
    Imprime el resultado en una cadena
"""
import datetime as dt

fecha_actual = dt.datetime.now().strftime('%d %B %Y, %I:%M:%S %p')
print(fecha_actual)

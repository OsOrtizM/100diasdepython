"""
Bienvenido al día 81 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para agregarle a la
        fecha actual 7 dias mas
            Imprime el resultado
"""
import datetime as dt

print(dt.date.today() + dt.timedelta(days=7))

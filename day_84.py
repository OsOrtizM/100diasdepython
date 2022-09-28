"""
Bienvenido al día 84 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para convertir la cadena
        "12-07-2022" a timestamp
            Imprime el resultado
"""
import datetime as dt

cadena = dt.datetime.strptime("12-07-2022", '%d-%m-%Y')
fecha = cadena.timestamp()
print(fecha)

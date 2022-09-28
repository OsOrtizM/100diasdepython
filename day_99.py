"""
Bienvenido al día 99 de #100diasdepython
            El reto de hoy es:
    Utiliza try para capturar e imprimir la
excepcion de una division entre 0 del siguiente
            fragmento de codigo
"""
try:
    a = 7
    b = a / 0
except ZeroDivisionError:
    print("Error! No se puede dividir entre 0")


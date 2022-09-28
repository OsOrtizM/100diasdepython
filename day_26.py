"""
Bienvenido al dia 26 de #100diasdepython
        El reto de hoy es:
Utiliza la funcion copy() para crear una
copia de la lista de compras utilizada en
el reto anteior, compara sus ids en memoria
e imprime el resultado
"""
from copy import copy

compras = ['leche', 'carne', 'pollo', 'huevos', 'embutidos']
copy_compras = copy(compras)
print(id(compras), id(copy_compras))

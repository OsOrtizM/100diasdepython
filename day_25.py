"""
Bienvenido al dia 25 de #100diasdepython
        El reto de hoy es:
Utiliza la lista de compras del reto anteior para
    contruir una cadena con saltos de linea
    sin usar ciclos e imprime el resultado
"""
compras = ['leche', 'carne', 'pollo', 'huevos', 'embutidos']

print(*compras, sep='\n')

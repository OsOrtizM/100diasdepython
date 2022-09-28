"""
Bienvenido al día 78 de #100diasdepython
            El reto de hoy es:
Utiliza itertools para unir las siguientes
    tuplas (78, 100) ("Dias", "Python")
    Obtiene el tipo de cada dato e
        imprimelo en una lista
"""
import itertools

tupla_1, tupla_2 = (78, 100), ("Dias", "Python")
union = list(itertools.chain(tupla_1, tupla_2))
tipos = list(map(type, union))
print(tipos)

"""
    Bienvenido al dia 40 de #100diasdepython
        El reto de hoy es:
Utiliza el conjunto del reto anterior y elimina
al gato del conjunto, si es que existiera, sin
usar sentencias condicionales e imprime el resultado
"""
conjunto = {'perro', 'gato', 'oso', 'aguila', 'pinguino'}
conjunto.discard('gato')
print(conjunto)

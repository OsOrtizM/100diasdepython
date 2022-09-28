"""
    Bienvenido al dia 60 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para capitalizar las
        palabras de la siguiente lista
["llevo", "sesenta", "dias", "programando", "wiii"]
        Imprime el resultado en nueva lista
"""


lista = ["llevo", "sesenta", "dias", "programando", "wiii"]
lista_capitalizada = list(map(lambda x: x.capitalize(), lista))

print(lista_capitalizada)

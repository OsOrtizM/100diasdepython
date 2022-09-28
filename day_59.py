"""
    Bienvenido al dia 59 de #100diasdepython
            El reto de hoy es:
Utiliza una funcion lambda para ordenar de forma
ascendente la siguiente lista de tuplas tomando el
        valor numerico como referencia
[("Quimica", 88), ("Fisica", 90), ("Lenguaje", 97)]
            Imprime el resultado
"""


lista = [("Quimica", 88), ("Fisica", 90), ("Lenguaje", 97)]
lista_ordeanda = sorted(lista, key=lambda x: x[1],)

print(lista_ordeanda)

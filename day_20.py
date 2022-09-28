"""
		Bienvenido al dia 20 de #100diasdepython
			    El reto de hoy es:
        De la siguiente cadena: 'PpYyTtHhOoNnIiSsTtAa'
Separa las mayusculas y minusculas sin usar ciclos en nuevas cadenas
        e imprime el resultado en una sola linea.
"""


cadena = 'PpYyTtHhOoNnIiSsTtAa'
maysc = cadena[::2]
minsc = cadena[1::2]

print(maysc, minsc)


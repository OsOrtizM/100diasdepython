"""
			    Bienvenido al dia 12 de #100diasdepython
					    El reto de hoy es:
Intercambia los valores de dos variables e imprime su ubicacion en memoria
                    utilizando la funucion id()
"""
number = 4
cadena = 'treinta'

number, cadena = cadena, number

print(id(number), id(cadena))



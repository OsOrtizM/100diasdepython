"""
		        Bienvenido al dia 18 de #100diasdepython
			            El reto de hoy es:
Declara una variable de tipo cadena, encuentra el primer y ultimo caraxter
            en orden lexicografico sin usar ciclos e imprimelos.
"""


cadena = 'aBEc3e1dAri2o'
res = sorted(sorted(cadena), key=str.upper)
print(res)


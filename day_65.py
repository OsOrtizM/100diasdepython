"""
    Bienvenido al día 65 de #100diasdepython
            El reto de hoy es:
Utiliza RegEx para quitar los prefijos telefonicos de los
            telefonos de la siguiente lista
["+54 11 1234 5678", "+591 68754321", "+56 98765 4321"]
Imprime una lista con los telefonos sin prefijos telefonicos
"""
import re

telefonos_extension = ["+54 11 1234 5678", "+591 68754321", "+56 98765 4321"]
telefonos_sin_extension = []
regex = re.compile(r'\+\d+ ')
for telefono in telefonos_extension:
    telefono_limpio = re.sub(regex, '', telefono)
    telefonos_sin_extension.append(telefono_limpio)

print(telefonos_sin_extension)

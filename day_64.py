"""
    Bienvenido al dia 64 de #100diasdepython
            El reto de hoy es:
Utiliza RegEx para quitar los ceros innecesarios
        de las direcciones IP de la lista
["192.08.001.5", "10.120.023.001", "192.160.2.1"]
    Imprime una lista con las IP validas
"""
import re

IPs = ["192.08.001.5", "10.120.023.001", "192.160.2.1"]
IPs_validas = []
regex = re.compile(r'^0*?([1-9]\d{0,2}.)0*?([1-9]\d{0,2}.)0*?([1-9]\d{0,2}.)0*?([1-9]\d{0,2})$')
for ip in IPs:
    captura = regex.search(ip)
    if captura:
        grupos = captura.group(1, 2, 3, 4)
        IPs_validas.append(grupos[0] + grupos[1] + grupos[2] + grupos[3])


print(IPs_validas)

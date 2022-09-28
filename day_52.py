"""
        Bienvenido al dia 52 de #100diasdepython
            El reto de hoy es:
Crea una funcion que convierta un numero entero en binario
                sin usar la funcion bin()
        El parametro de entrada es un numero entero
        EL valor de salida es una cadena del valor
                del numero binario
        Ejecuta la funcion para el numero 52
                Imprime el resultado
"""


def int_to_bin(entero):
    binario = ''
    while entero > 1:
        binario += str(entero % 2)
        entero //= 2
    if entero:
        binario += '1'
    return binario[::-1].zfill(8)


print(int_to_bin(52))

"""
    Bienvenido al dia 62 de #100diasdepython
            El reto de hoy es:
    Utiliza RegEx para validar la lista de emails
        ["pythonlapaz@gmail.com", "dias.com",
    "comidita@.com", "programando@outlook.com"]
        Imprime una lista con los emails validos
"""
import re

lista = ["python.lapaz@gmail.com", "dias.com", "comidita@.com", "programando@outlook.com"]
regex = re.compile(r'^\w+[._]?\w+@\w+[.]\w+$')
lista_emails = list(filter(lambda x: regex.fullmatch(x) is not None, lista))

print(lista_emails)

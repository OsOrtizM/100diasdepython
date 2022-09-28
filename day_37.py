"""
    Bienvenido al dia 37 de #100diasdepython
            El reto de hoy es:
Utiliza el diccionario de palabras del reto
anterior para eliminar todos los elementos del
diccionario sin usar ciclos, imprime el resultado
"""
diccionario = dict({
    'algoritmo': 'Método que describe cómo se resuelve un problema en término de las acciones que se ejecutan y '
                 'especifica el orden en que se ejecutan estas acciones. Los algoritmos ayudan al programador a '
                 'planificar un programa antes de su escritura en un lenguaje de programación.',
    'clase': 'Colección encapsulada de datos y operaciones que actúan sobre los datos. El concepto de clase es '
             'fundamental en programación orientada a objetos. Una clase consta demétodos y datos. Los métodos de una '
             'clase definen el conjunto de operaciones permitidas sobre los datos de una clase (sus atributos). Una '
             'clase puede tener muchas instancia de la clase u objetos.',
    'comentario': 'Trozo de texto que tienen como objetivo documentar el programa y mostrar como se ha construido. '
                  'Los comentarios no son sentencias de programación y son ignorados por el compilador.',
    'framework': 'Un entorno de trabajo o marco de trabajo es un conjunto estandarizado de conceptos, prácticas y '
                 'criterios para enfocar un tipo de problemática particular que sirve como referencia, para enfrentar '
                 'y resolver nuevos problemas de índole similar.',
    'depuracion': 'Proceso de encontrar, fijar y eliminar errores en un programa. Para estas tareas se suele utilizar '
                  'una herramienta de programación conocida como depurador.'

})
diccionario['python'] = 'Lenguaje de programacion multiparadigma'
diccionario.pop('algoritmo')
diccionario.clear()
print(len(diccionario))

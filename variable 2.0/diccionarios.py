#creando diccionario
diccionario = dict(nombre="Abdiel", apellido="Murillo") #con dict se puede crear diccionarios vacios, de la otra manera tradicional no se puede (APLICA PARA LISTAS, TUPLAS)
#las listas no pueden ser claves(almenos que lo coloques dentro de la funcion forzen set), las tuplas si
diccionario = {frozenset(["abdiel","murillo"]): "Nombre y su apellido"}

#creando diccionarios con frontkeys valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])     #el resultado sera {'nombre': None, 'apellido': None

#creando diccionarios con frontkeys cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"no se")  #{'nombre': 'no se', 'apellido': 'no se'}

print(diccionario)


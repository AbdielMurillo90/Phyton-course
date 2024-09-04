#Modificable
lista =["nombre","edad",True,False,1.85] 
lista[0] = "Apellidos" #ejemplo de como modificar una lista

tupla = ("nombre","edad",True,False,1.85)  #No se puede modificar
print(lista[0])

#Creando un conjunto (set) utilizan llaves {}
#Conjunto no puede acceder por indice
#no almacena datos duplicados
#son datos desordenados
conjunto = {"nombre","edad",True,False,1.85}

#creando diccionario
#Para acceder a los datos, tiene que ser por su nombre, no por su indice como en las tuplas y lsitas
#marcando un diccionario
# se separan por comas
diccionario = {
    "nombre": "Abdiel Murillo",
    "Hobbies": "jugar",
    "edad": 4
}

print(diccionario["nombre"])
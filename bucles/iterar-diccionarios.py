diccionario = {
    "nombre": "Abdiel",
    "apellido": "murillo",
    "edad": 25
}
#En este bucle itera sobre las keys solamente
for key in diccionario:
    print(key)

#añadiendo el metodo .items() se podra
for key in diccionario.items():
    print(key)
#imprimira esto:
# ('nombre', 'Abdiel')
# ('apellido', 'murillo')
# ('edad', 25)

for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"Dentro del diccionario, la llave {key} mostrara el valor de {valor}")
diccionario = {
    "nombre": "Abdiel",
    "apellido": "murillo",
    "edad": 25
}
#En este bucle itera sobre las keys solamente
for key in diccionario:
    print(key)

#añadiendo el metodo .items() se podra ver clvae: valor en formato de tuplas
for key in diccionario.items():
    print(key)
#imprimira esto:
# ('nombre', 'Abdiel')
# ('apellido', 'murillo')
# ('edad', 25)

#recorriendo un diccionario con items() para obtener clave y valor
for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"Dentro del diccionario, la llave {key} mostrara el valor de {valor}")
# Dentro del diccionario, la llave nombre mostrara el valor de Abdiel
# Dentro del diccionario, la llave apellido mostrara el valor de murillo
# Dentro del diccionario, la llave edad mostrara el valor de 25

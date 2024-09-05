frutas = ["banana","sandia","pera","granada","uva","cereza","fresa"]
dislike = input("Estas son las frutas disponibles, muestra o escribe excatamente cual no te gusta: banana, sandia, pera, granada, uva, cereza, fresa \n")
texto = "Abdiel"
numeros = [2,5,8,9]

#Estableciendo condiciones
for escoger in frutas:
    if escoger == dislike:
        continue #este comando omite o skipea ese elemento
    print(f"me llevare las siguientes frutas: {escoger}")
# me llevare las siguientes frutas: banana
# me llevare las siguientes frutas: pera
# me llevare las siguientes frutas: granada
# me llevare las siguientes frutas: uva
# me llevare las siguientes frutas: cereza
# me llevare las siguientes frutas: fresa

#para romper el ciclo apenas se presente la condicion, es break(con break, el else no se ejecutaria (else equivale al print, en este caso el print si puede pero el else no))
for escoger in frutas:
    if escoger == dislike:
            break
    print(f"me llevare las siguientes frutas: {escoger}")

print("el bucle ha terminado")

#Recorrer una cadena (iterar)
for l in texto:
    print(l)


#for en una sola linea de codigo (se quiere duplicar los numeros dentro de una lista) aqui primero se realiza la expresion que quiere que haga la variable que pertenecera al bucle, en este caso x ya tenia el valor de x*2 al entrar en un bucle
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
#[4, 10, 16, 18]
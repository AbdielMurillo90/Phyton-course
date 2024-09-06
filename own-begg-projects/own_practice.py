frutas = ["banana","sandia","pera","granada","uva","cereza","fresa","naranja","mandarina"]
frutas_llevar = []
precio = [2,4,3.5,1.32,4.21,3.5,4,6.12]
frutas_precios = dict(zip(frutas,precio)) #zip lo que hace es: oma dos (o más) iterables (como listas) y los combina en pares. Cada par contiene un elemento de cada iterable en la misma posición.
print (frutas_precios)

def compras ():
    x = 1
    precio_final = 0
    while x==1:
        quest = input("Estas son las frutas disponibles, muestra o escribe excatamente que frutas deseas llevar:  (escribe 1, enter y luego el siguiente): \n")
        quest.lower()
        if quest in frutas:
            cantidad= int(input("introduce la cantidad: "))
            costo = cantidad * frutas_precios[quest]
            frutas_llevar.append((quest,cantidad)) #El append no permite en una lista mas de un valor, una tupla si
            precio_final += costo
            quest2 = input("deseas llevar otra fruta?(Y/N): \n")
            if quest2 == "Y":
                print(f"Esta son las que llevas de momento(fruta,cantidad): {frutas_llevar},  y el precio total es: {costo} ")
            
            else:
                x =2
        else:
            ("fruta no disponible, Por favor, elige 1 de la lista")
    return frutas_llevar, precio_final
            
#aca se procede a llamar la funcion y desempaquetar los returns
frutas_llevar, precio_final = compras()

print(f"tus frutas fueron {frutas_llevar} y el total es: {precio_final}")




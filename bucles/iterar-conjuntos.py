animales= {"perro","gato","loro","capybara","jirafa"}
numeros = {1,3,4,6,8}

#recorriendo la conjunto animales

for animal in animales: #La variable animal es una variable que unicamente se usara dentro del bucle 
    print(f"ahora la variable animal es: {animal}")
    
#recorriendo la conjunto numeros
for num in numeros:
    print(f"El {num} multplicado por 2, es igual a: {num*2}")
    
#iterando 2 conjuntos, un for dentro de un for(deben poseer la misma cantidad de elementos) se utiliza zip(es una funcion). Itera al mismo tiempo.
for animal,number in zip(animales,numeros):
    print(f"recorriendo la conjunto numero 1(animal): {animal} y la conjunto numero(number): {number}")
#este es el resultado:
# recorriendo la conjunto numero 1(animal): perro y la conjunto numero(number): 1
# recorriendo la conjunto numero 1(animal): gato y la conjunto numero(number): 3
# recorriendo la conjunto numero 1(animal): loro y la conjunto numero(number): 4
# recorriendo la conjunto numero 1(animal): capybara y la conjunto numero(number): 6
# recorriendo la conjunto numero 1(animal): jirafa y la conjunto numero(number): 8

#Utilizando in range en el bucle for:
for num in range(0,10+1):
    print(num)



#forma optima de recorrer una conjunto con su indice (enumerate): muestra el indice y el valor de ese indice
for num in enumerate(animales):
    indice = num[0]
    valor = num[1]
    print(f"este bucle va a mostrar el indice {indice} en la conjunto animales, por lo cual es: {valor} ")
    #print(f"el indice es: {Indice} y el valor es: {valor}")

#forma elegante desempaquetando (la verdadera forma) enumerate hace dos cosas: contar la cantidad de elementos (como si fuera len) para iterar, lo cual tambien hace la funcion como si fuera un indice, y ademas muestra el valor de la variable
#en este caso creamos dos variables para el bucle for, en donde el primero almacena el indice y el segundo almacena el valor de la variable que queremos (la que estara dentro de enumerate)
#luego debemos indicarlo dentro del bucle for
for numero,animal in enumerate(animales):
    indice = numero
    valor = animal
    print(f"este bucle va a mostrar el indice {indice} en la conjunto animales, por lo cual es: {valor} ")


#usando for/else:
for numero in numeros:
    print(f"ejecutnado el ultimo bucle, valor actual:{numeros}")
else: 
    print("el bucle ha finalizado")
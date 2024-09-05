animales= ["perro","gato","loro","capybara","jirafa"]
numeros = [1,3,4,6,8]

#recorriendo la lista animales

for animal in animales: #La variable animal es una variable que unicamente se usara dentro del bucle
    print(f"ahora la variable animal es: {animal}")
    
#recorriendo la lista numeros
for num in numeros:
    print(f"El {num} multplicado por 2, es igual a: {num*2}")
    
#iterando 2 listas, un for dentro de un for(deben poseer la misma cantidad de elementos) se utiliza zip(es una funcion). Itera al mismo tiempo.
for animal,number in zip(animales,numeros):
    print(f"recorriendo la lista numero 1(animal): {animal} y la lista numero(number): {number}")
#este es el resultado:
# recorriendo la lista numero 1(animal): perro y la lista numero(number): 1
# recorriendo la lista numero 1(animal): gato y la lista numero(number): 3
# recorriendo la lista numero 1(animal): loro y la lista numero(number): 4
# recorriendo la lista numero 1(animal): capybara y la lista numero(number): 6
# recorriendo la lista numero 1(animal): jirafa y la lista numero(number): 8

#Utilizando in range en el bucle for:
for num in range(0,10+1):
    print(num)

#forma no optima para recorrer una lista
for num in range(len(numeros)):
    print(f"este bucle va a mostrar el indice {num} en la lista animales, por lo cual es: {animales[num]}")
#este es el resultado:
# este bucle va a mostrar el indice 0 en la lista animales, por lo cual es: perro
# este bucle va a mostrar el indice 1 en la lista animales, por lo cual es: gato
# este bucle va a mostrar el indice 2 en la lista animales, por lo cual es: loro
# este bucle va a mostrar el indice 3 en la lista animales, por lo cual es: capybara
# este bucle va a mostrar el indice 4 en la lista animales, por lo cual es: jirafa

#forma optima de recorrer una lista con su indice (enumerate): muestra el indice y el valor de ese indice
for num in enumerate(animales):
    indice = num[0]
    valor = num[1]
    print(f"este bucle va a mostrar el indice {indice} en la lista animales, por lo cual es: {valor} ")
    #print(f"el indice es: {Indice} y el valor es: {valor}")

#forma elegante desempaquetando
for numero,animal in enumerate(animales):
    indice = numero
    valor = animal
    print(f"este bucle va a mostrar el indice {indice} en la lista animales, por lo cual es: {valor} ")

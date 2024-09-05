#Creando un conjunto con set

conjunto = set(["abdiel","murillo"])

#meter un conjunto dentro de otro conjunto
conjunto1 = frozenset({"dato1","dato2"})
conjunto2 = {conjunto1,"dato3"}
#print(conjunto2)

#teoria de conjuntos( issubset =subconjunto) este es un metodo
conjunto1 = {21,23,25,26,27}
conjunto2 = {22,28}

resultado = conjunto2.issubset(conjunto1)
resultado_alternativo = conjunto2 <= conjunto1

#Verificar si es un superconjunto (issuperset)
resultado_superconjunto= conjunto1.issuperset(conjunto2)
resultado_alternativo2 = conjunto1 > conjunto2

#verificar si hay algun numero en comun entre los conjuntos
resultado_verificar = conjunto2.isdisjoint(conjunto1) #cuando es false, es porque hay numeros en comun; de ser True, no lo hay.

print(resultado_verificar)
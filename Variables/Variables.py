#numero = 10
#numero += 1  #Lo que hace esto es hacerlo acumulativo: seria numero = numero + 1

#en caso tal se desee concatenar
primer_saludo = "Abdiel"
Saludo_completo = "Hola " + primer_saludo + ", ¿Cómo estás?"
print(Saludo_completo)

#Otra forma de concatenar
primer_saludo = "Abdiel"
Saludo_completo = f"Hola {primer_saludo} , ¿Cómo estás?"
print(Saludo_completo)

#Operadores de pertenencia(in, not in)
print("abd" in Saludo_completo)
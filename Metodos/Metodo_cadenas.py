chain1 ="Hi, my name is Abdiel Murillo"
chain2 ="You´re the best gacha player I ever seen"

#Cunado es funcion, va entre parentesis. Cuando son metodos deben ir con un punto y luego la funcion: dato.metodo()
mayuscula= chain1.upper()
minuscula = chain2.lower()
capital = chain1.capitalize() + chain2.capitalize()


#buscamos una cadena en otra, es el find. Devuelve la ubicacion o el indice de lo que queremos buscar(python es sensible a mayusculas y minusculas)
Find_method = chain1.find("y") #devolvera 5

#buscamos una cadena con otra, con la diferencia que, si no encuentra, arrojara una excepcion
index_mehtod= chain2.index("a")

#si es numerico, devuelve True, de lo contrario False
isnumeric_method= chain1.isnumeric()

#si es alfanumerico, devuelve True, de lo contrario False(en ese caso, solamente oma en cuenta las letras del abecedario de la A hasta la Z, sin contar los espacios)

#este metodo Devuelve la cantidad de caracteres que se le indica
count_method= chain2.count("a") 

#este es una FUNCION que cuenta la cantidad de caracteres en general que posee una cadena de caracteres

len_fuction = len(chain1)

#Este es un metodo, que indica si una cadena empieza con una cadena; de ser asi mostrara TRUE
startwith_method = chain1.startswith("m")

#Este metodo indica si una cadena termina con una cadena; de ser asi mostrars True
endwith_method = chain1.endswith("o")

#Este metodo remplaza una cadena, con otra cadena
replace_method = chain1.replace("Abdiel","Misael")

#este metodo separara las cadenas con las cadenas que le indicamos para separar, convirtiendolo en una lista: ['You´re', 'the', 'best', 'gacha', 'player', 'I', 'ever', 'seen']
split_method= chain2.split(" ")
print(split_method[2])

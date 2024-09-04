datos= input("introduce unas palabras: ").split(" ")
# calcular cuantas frases dijo
amount_words= len(datos)
time = amount_words * (1/2)
# calculate how much time will take to say all thats words, knowing that: 1 second = 2 words

print(f"the amount of words are: {amount_words} and the time that take it are: {time} seconds")
#If take more of 60 seconds, then say: "I dont want your whole story dude!!!"
if time > 60:
    print("I dont want your whole story dude!!!")

#Dalto speaks 30% faster than regular person, how much time he takes?
dalto_time = time/ 1.3
print(f"dalto speaks thats words in {dalto_time: .1f} seconds")

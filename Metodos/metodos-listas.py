#creando una lista con list
lista = list(["Abdiel","murillo",25])

amoun_of_element= len(lista)
#agregando elementos a una lista con append
lista.append("1.74")

#The insert method adds a string element to a list but, we need to especify the index
lista.insert(2,"misael")

#the extend method adds more than one items to a list and we need to create a list in this method to add the item to the final of list.
lista.extend(["Like anime","Play games"])

#Pop method removes an item from a list (must specify the index)
# Interesting life hack: If we want remove the last item from a list using pop(that need an index), we type -1 or any negative number.
lista.pop(-1)

# The remove method: removes an item from a list  by typing the item that we want to remove
lista.remove("misael")

# The clear method removes all items from a list
#lista.clear()

#The sort method order by ascending order (only accepts number and boolean items)
#curius lifehack: If we write reverse = true in the sort method, it does the same thing but in reverse. (descending)
#lista.sort(reverse = True)

#the reverse method reverse the all list, ignoring if its a string or int.
lista.reverse()

#The index in list, find an item that we will write into it
finding_element = lista.index("Abdiel")

print(finding_element)
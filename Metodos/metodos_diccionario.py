# Remember: in dictionary we cannot accces or print by index, is by the name
dictionary = {
    "fruit" : "Apple, juice and other healthy fruits",
    "materials" : "blocks, concrete",
    "games" : "ff xv, minecraft, the witcher",
    "numbers": 12314
}

#key method: We can acces to the keys of a dictionary.
keys = dictionary.keys()
print(keys)

# get method: We can access to the values from the keys of a dictionary
values = dictionary.get("fruit")
print(values)

#clear method: removes everything from the list
    #clear_method= dictionary.clear()

#pop method: remove an item from the list but we need to specify, what item we want to remove
dictionary.pop("fruit")
print(dictionary.keys())

#obteniendo un elemento dict_items iterable:
iterable_dictionary= dictionary.items()
print(iterable_dictionary)






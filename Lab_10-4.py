#Author Sean Salafia 1/23/23

def indexed_names(names):
    indexed_names = []     #Creates open list to be modified
    for index,name in enumerate(names):
        indexed_names.append(index,name)
        return indexed_names

print(indexed_names(["Jim","James"]))
print(indexed_names(["Tommy","Ruth","Kathy"]))

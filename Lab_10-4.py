#Author Sean Salafia 1/23/23

def indexed_names(names):
    indexed_names = []     #Creates open list to be modified
    for index,name in enumerate(names):
        indexed_names.append("{}: {}".format(index,name))   #(Searched up) Format fucntion combines the two strings into one for the list to be appended 
        continue    # Loops back to the beginning to complete checking the whole list input
    return indexed_names

#Test Cases
print(indexed_names(["Jim","James"]))
print(indexed_names(["Tommy","Ruth","Kathy"]))

#DONE 
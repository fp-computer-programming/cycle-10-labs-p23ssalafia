#Author: Sean Salafia 1/23/23


def double_stuff(stuff):    #Creates function, takes list of stuff
    for index,value in enumerate(stuff):        #Enumeration statment tracks index lets the fucntion loop
        stuff[index] = value * 2        #Multiplies whatever is in the index by 2
    return stuff


print(double_stuff ([5]))
print(double_stuff([5,456093458.032]))
print(double_stuff ([1,'apple', 1.52]))

#DONE 
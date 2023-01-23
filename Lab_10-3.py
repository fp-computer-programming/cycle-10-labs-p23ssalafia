#Author: Sean Salafia 1/23/23


def double_stuff(stuff):
    for index,value in enumerate(stuff):
        stuff[index] = value * 2
    return stuff


print(double_stuff ([5]))
print(double_stuff([5,456093458.032]))
print(double_stuff ([1,'apple', 1.52]))


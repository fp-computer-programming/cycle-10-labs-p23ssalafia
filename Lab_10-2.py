#Author: Sean Salafia 1/23/23
n = []      #Creates open list

while True:             #While true
    input_number = int(input("Input number here: "))    #User inputs #
    if input_number == -1:      #If it is -1, code breaks
        break
    elif input_number % 3 == 0:     #If It is divisible by 3, appends list to add the number
        n.append(input_number)
    else:                       #Else, do the continue function which takes it back to the top letting the user restart the loop.
        continue

print("Multiples of 3: ", n)        #Prints multiples of 3

#DONE


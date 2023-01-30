#Author: Sean Salafia 1/26/23

sum = 0  #Start sum at 0

while True:           #While the number is -1, print sum, otherwise, do the equation sum + num where num is the input.
    num = int(input("Input a number here: " ))
    if num == -1:
        print(sum)
        break
    sum += num

#DONE 
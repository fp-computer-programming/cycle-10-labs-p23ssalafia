#Author: Sean Salafia 1/26/23

sum = 0  #Start sum at 0

while True:           #While the number is -1, print sum, if not true, do sum + num
    num = int(input("Input a number here: " ))
    if num == -1:
        print(sum)
        break
    else:
        sum += num


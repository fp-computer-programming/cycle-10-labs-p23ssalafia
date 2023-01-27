#Author: Sean Salafia 1/23/23
n = []

while True:
    input_number = int(input("Input number here: "))
    if input_number == -1:
        break
    elif input_number % 3 == 0:
        n.append(input_number)
    else:
        continue

print("Multiples of 3: ", n)


#Author: Sean Salafia 1/25/23

def add_nums(numbers):
    num_list = []
    try:
        user_input = input("Input a list of numbers: ")
        num_list.append(numbers)
    except TypeError:
        print("Error Encountered. Please enter a valid number.")
    finally:
        print("The number list is: " + num_list)
        print("Your final input was: " + user_input)
    return()

print(add_nums[1,2,3,4,5])


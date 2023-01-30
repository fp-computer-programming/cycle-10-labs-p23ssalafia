def add_nums(numbers):  #Creates function
    user_input = []        #User input starts as empty list where user will input a number
    while True:
        try:
            user_input = int(input("Enter a number: ")) #User inputs
            break       #break
        except ValueError:          #if value error, go back and re enter input
            print("Invalid input. Please enter a number.")
        except TypeError:           #if Type error go back and re enter input
            print("Invalid input. Please enter a number.")
        finally:                    #Always show the passed list and what the user input was, using the format method to act as a place holder for numbers and the user input
            print("Passed list: {} ; user input: {} ".format(numbers, user_input))
    
    result = [num + user_input for num in numbers]
    return result

# Test cases
print(add_nums([1, 2, 3, 4]))
print(add_nums([0, -1, -2, -3]))
print(add_nums([10, 20, 30, 40]))

#DONE 
#Author: Sean Salafia    

def add_foods(foods):
    sixth_letter = []       #Creates a bunch of lists to be appended
    not_foods = []
    short_foods = []
    for food in foods:
        try:
            if len(food) >= 6:                  #If length of input is more than 6, add the 6th letter to a list sixth letter
                sixth_letter.append(food[5])
            else:                               #If length of input is less than 6 add to short foods
                short_foods.append(food)
        except :                                 #If any error occurs, like a type error, add the input to not foods
            not_foods.append(food)
            
    return("Sixth Letter: ", sixth_letter,"Not Foods :", not_foods,"Short Foods: ", short_foods)        #return

#Test Cases
print(add_foods(['potatoes','salsa','cherries','banana','apple']))
print(add_foods(['naan','celery','buckwheat',7,'clementine']))
print(add_foods(['cheeseburger',True,'chicken','rice','radish']))

#DONE 
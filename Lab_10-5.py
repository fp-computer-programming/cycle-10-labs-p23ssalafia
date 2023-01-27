#Author: Sean Salafia 1/25/23


def add_foods(food):
    six_letter_foods = []
    not_foods = []
    short_foods = []
    for index,variables in enumerate(food):
        try:
            food_string = str(variables)
            if len(food_string) >= 8:
                six_letter_foods.append(food_string)
            else:
                short_foods.append(food_string)
        except TypeError:
            not_foods.append(food_string)
        except IndexError:
            short_foods.append(food_string)

    return("Six Letter Foods: ", six_letter_foods,"Not Foods :", not_foods,"Short Foods: ", short_foods)

print(add_foods(['potoatoes','salsa','cherries','banana','apple']))
print(add_foods(['naan','celery','buckwheat',7,'clementine']))
print(add_foods(['cheeseburger',True,'chicken','rice','radish']))

#WIP

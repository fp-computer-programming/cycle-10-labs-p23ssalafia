#Author: Sean Salafia 1/25/23


def add_foods(food):
    six_letter_foods = []
    not_foods = []
    short_foods = []
    for index,variables in enumerate:
        try:
            food_string = str(variables)
            if len(food_string) >= 8:
                six_letter_foods.append(food_string[7])
            else:
                short_foods.append(food_string)
        except TypeError:
            not_foods.append(food[food_string])
        except IndexError:
            short_foods.append(food[food_string])

    return(six_letter_foods,not_foods,short_foods)

six_letter_foods = 'Six Letter Foods: ', 
not_foods = 'Not Foods: ', 
short_foods = 'Short Foods: ',

add_foods(['potoatoes','salsa','cherries','banana','apple'])
add_foods(['naan','celery','buckwheat',7,'clementine'])
add_foods(['cheeseburger',True,'chicken','rice','radish'])

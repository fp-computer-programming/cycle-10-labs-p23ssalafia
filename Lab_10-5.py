#Author: Sean Salafia 1/25/23


def add_foods(food):
    six_letter_foods = []
    not_foods = []
    short_foods = []
    food_index = []
    try:
        for index,variables in enumerate:
            foodx  = [*variables]
            six_letter_foods.append(foodx[7])
    except TypeError:
        not_foods.append(food[food_index])
    except IndexError:
        short_foods.append(food[food_index])

    six_letter_foods = 'Six Letter Foods: ', 
    not_foods = 'Not Foods: ', 
    short_foods = 'Short Foods: ',

    return(six_letter_foods,not_foods,short_foods)


add_foods(['potoatoes','salsa','cherries','banana','apple'])
add_foods(['naan','celery','buckwheat',7,'clementine'])
add_foods(['cheeseburger',True,'chicken','rice','radish'])

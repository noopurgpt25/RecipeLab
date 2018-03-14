from constants import *
import re
import random
import math

def incrementNumbers(statement):
    # number1 = int(input('What number would you like to increment?')
    # number2 = number1 + 1
    for numbers in statement:
        if numbers.isdigit():
            number2 = int(numbers) 
            statement = statement.replace(numbers,str(number2))
    return statement

def decrementNumbers(statement):
    # number1 = int(input('What number would you like to increment?')
    # number2 = number1 + 1
    for numbers in statement:
        if numbers.isdigit():
            number2 = math.ceil(int(numbers)/2)
            statement = statement.replace(numbers,str(number2))
    return statement

def fry2bake(ingredientList, preparationList):
    new_prep_ingred = []
    for item in ingredientList:
        new_item = item
        for key in fry2bakeMethods.keys():
            if key in new_item:
                new_item = new_item.replace(key, fry2bakeMethods[key])
        new_prep_ingred.append(new_item)

    step1 = "Preheat the oven for 10 min"
    new_prep_list = []
    for step in preparationList:
        step = incrementNumbers(step)
        # print (step)
        new_step = step
        for key in fry2bakeMethods.keys():
            if key in new_step:
                new_step = new_step.replace(key, fry2bakeMethods[key])

        new_prep_list.append(new_step)
    new_prep_list.insert(3,step1)
    return new_prep_ingred, new_prep_list


def bake2fry(ingredientList, preparationList):
    # remove preheat oven line
    del preparationList[3]
    # print (preparationList)

    new_prep_ingred = []
    for item in ingredientList:
        new_item = item
        for key in bake2fryMethods.keys ():
            if key in new_item:
                new_item = new_item.replace (key, bake2fryMethods[key])
        new_prep_ingred.append (new_item)

    new_prep_list = []
    for step in preparationList:
        step = decrementNumbers(step)
        new_step = step
        for key in bake2fryMethods.keys():
            if key in new_step:
                new_step = new_step.replace(key, bake2fryMethods[key])
        new_prep_list.append(new_step)

    return new_prep_ingred, new_prep_list
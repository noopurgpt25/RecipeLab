from constants import *
import re

def makeHealth(ingredientList, preperationList):
	for ingredient in ingredientList:
		name=ingredient.get('name')
		for item in unHealthItems:
			if bool(re.match(".(?i)*"+item+".*",name)):
				if "amount" in ingredient:
					ingredient["amount"]= ingredient.get("amount")/2
					break
		for meat in readMeats:
			name=ingredient.get('name')
			if bool(re.match(".(?i)*"+meat+".*",name)):
				if "amount" in ingredient:
					newItem=re.sub(".(?i)*"+meat,"chicken",name)
					ingredient['name']=newItem
					break
	count=0
	for step in preperationList:
		newItem=step
		for meat in readMeats:
			newItem=newItem.replace(meat, "chicken")
		preperationList[count]=newItem
		#print(preperationList[count])
		count+=1
	return preperationList


def makeUnhealthy(ingredientList, preperationList):
	for ingredient in ingredientList:
		name=ingredient.get('name')
		for item in healthierItems:
			if bool(re.match(".(?i)*"+item+".*",name)):
				ingredient['name']="lard"
	for ingredient in ingredientList:
		name=ingredient.get('name')
		for item in unHealthItems:
			if bool(re.match(".(?i)*"+item+".*",name)):
				if "amount" in ingredient:
					ingredient["amount"]= ingredient.get("amount")*2
					break
	count=0
	for step in preperationList:
			newItem=step
			for food in unHealthItems:
				newItem=newItem.replace(food, "lard")

			preperationList[count]=newItem
			count+=1
	return preperationList
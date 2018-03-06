from constants import *
import re

def makeVegitarian(ingredientList, preperationList, categoryList):
	if "Vegetarian" in categoryList or "Vegan" in categoryList:
		return preperationList

	for ingredient in ingredientList:
		name=ingredient.get('name')
		for meat in meats:
			if bool(re.match(".(?i)*"+meat+".*",name)):
				newVeg=meatToVegDict.get(meat)
				if newVeg==None:
					newVeg="tofu"
				newItem=re.sub(".(?i)*"+meat,newVeg,name)
				ingredient['name']=newItem
				break
	count=0
	for step in preperationList:
		newItem=step
		for meat in meats:
			newVeg=meatToVegDict.get(meat)
			#print(meat)
			newItem=newItem.replace(meat, newVeg)

			#if bool(re.match(".(?i)*"+meat+".*",step)):
			#	newVeg=meatToVegDict.get(meat)
			#	if newVeg==None:
			#		newVeg="tofu"
			#	newItem=re.sub(".(?i)*"+meat,newVeg,step)
		preperationList[count]=newItem
		#print(preperationList[count])
		count+=1
	return preperationList


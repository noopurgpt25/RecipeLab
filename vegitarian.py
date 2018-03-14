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
			if newVeg==None:
				newVeg="tofu"
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

def makeVegan(ingredientList, preperationList, categoryList):
	if "Vegan" in categoryList:
		return preperationList
	for ingredient in ingredientList:
		name=ingredient.get('name')
		for meat in meatToVeganDict.keys():
			if bool(re.match(".(?i)*"+meat+".*",name)):
				newVeg=meatToVeganDict.get(meat)
				if newVeg==None:
					newVeg="tofu"
				newItem=re.sub(".(?i)*"+meat,newVeg,name)
				ingredient['name']=newItem
				break
	count=0
	for step in preperationList:
		newItem=step
		for meat in meatToVeganDict.keys():
			newVeg=meatToVeganDict.get(meat)
			if newVeg==None:
				newVeg="tofu"
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

def makeNonVegitarian(ingredientList, preperationList, categoryList):
	hasMeat=False
	if "Vegetarian" in categoryList: 
		categoryList.remove("Vegetarian")
	if "Vegan" in categoryList:
		categoryList.remove("Vegan")
	for ingredient in ingredientList:
		name=ingredient.get('name')
		for meat in meats:
			if bool(re.match(".(?i)*"+meat+".*",name)):
				return preperationList, categoryList

	for ingredient in ingredientList:
		name=ingredient.get('name')
		for veg in vegitarianProteins:
			if bool(re.match(".(?i)*"+veg+".*",name)):
				newVeg=vegToMeatDict.get(veg)
				if newVeg==None:
					newVeg="chicken"
				newItem=re.sub(".(?i)*"+veg,newVeg,name)
				ingredient['name']=newItem
				hasMeat=True
				break
	count=0
	print(hasMeat)
	if hasMeat:
		for step in preperationList:
			newItem=step
			for veg in vegitarianProteins:
				newVeg=vegToMeatDict.get(veg)
				if newVeg==None:
					newVeg="chicken"
				newItem=newItem.replace(veg, newVeg)

			preperationList[count]=newItem
			count+=1
	else:
		tempDict={}
		tempDict["amount"]=1
		tempDict["amount_type"]="sprinkle"
		tempDict["name"]="bacon bits"
		preperationList.append("Sprkinkle bacon bits on top of the dish.")
	return preperationList,categoryList

def makeNonVegan(ingredientList, preperationList, categoryList):
	hasMeat=False
	if "Vegan" in categoryList:
		categoryList.remove("Vegan")
	for ingredient in ingredientList:
		name=ingredient.get('name')
		for meat in meats:
			if bool(re.match(".(?i)*"+meat+".*",name)):
				return preperationList, categoryList

	for ingredient in ingredientList:
		name=ingredient.get('name')
		for veg in meatToVeganDict.keys():
			if bool(re.match(".(?i)*"+meatToVeganDict[veg]+".*",name)):
				newVeg=veg
				#if newVeg==None:
				#	newVeg="chicken"
				newItem=re.sub(".(?i)*"+veg,newVeg,name)
				ingredient['name']=newItem
				hasMeat=True
				break
	count=0
	print(hasMeat)
	if hasMeat:
		for step in preperationList:
			newItem=step
			for veg in meatToVeganDict.keys():
				newVeg=veg
				if newVeg==None:
					newVeg="chicken"
				newItem=newItem.replace(meatToVeganDict[veg], newVeg)

			preperationList[count]=newItem
			count+=1
	else:
		tempDict={}
		tempDict["amount"]=1
		tempDict["amount_type"]="sprinkle"
		tempDict["name"]="bacon bits"
		preperationList.append("Sprkinkle bacon bits on top of the dish.")
	return preperationList,categoryList


from constants import *
import re


def makeMexican(ingredientList, preperationList, foodCategories):
	proteins=[]

	count=0
	#Categorized as mexican no need to further look
	if "Mexican" in foodCategories:
		return preperationList
	#If it is a Dessert it is completly different transformation
	if "Desserts" in foodCategories:
		for key in mexicanDesertIngreDict:
			is_present=False
			for item in ingredientList:
				name = item.get("name");
				if bool(re.match(".(?i)*"+name+".*",str(key))):
					is_present=True
					count+=1
					break
			if(count>=2):
				#Has many mexican ingredients in it so probably mexican even though not categorized as such
				return preperationList
			if (not is_present):
				temp_dict={};
				temp_dict['name']=key;
				holder=mexicanDesertIngreDict.get(key);
				splitAmount=holder.split()
				if (len(splitAmount)>1):
					temp_dict['amount']=int(splitAmount[0]);
					if splitAmount[1] in measurements:
						temp_dict['amount_type']=splitAmount[1];
					else:
						i=2
						temp_dict['notes']=splitAmount[1]
						while (i<len(splitAmount)):
							temp_dict['notes']=temp_dict.get('notes')+" "+splitAmount[i];
							i+=1
				else:
					temp_dict['amount']=int(splitAmount[0]);
				ingredientList.append(temp_dict)
		newSteps="Add to mixture"
		stepCounter=0
		check=False
		for item in mexicanDesertIngredient:
			newSteps=newSteps+" "+item
		for step in preperationList:
			if "batter" in step or "filling" in step: 
				findBatter=step.split(".")
				holder=[]
				j = 0
				while j<len(findBatter):
					#print(check)
					holder.append(findBatter[j])
					if(check and "batter" in findBatter[j] or "filling" in findBatter[j]):
						holder.append(newSteps)
						check = False
					j+=1
				holder=" ".join(holder)
				preperationList[stepCounter]=holder
				break
			stepCounter+=1
		return(preperationList)
	#Not Mexican and not a desert
	for item in ingredientList:
		present=True;
		name = item.get("name");
		for subKey in mexicanSubsDict:
			if bool(re.match(".(?i)*"+subKey+".*",name)):
				item["name"]=mexicanSubsDict.get(subKey);
		for food in nonMexicanIngredinet:
			if bool(re.match(".(?i)*"+food+".*",name)):
				ingredientList.remove(item);
				present =False;
				break
		if present:
			for meat in meats:
				if bool(re.match(".(?i)*"+meat+".*",name) and not (name in soups)):
					proteins.append(name);
					break
			for veg in vegitarianProteins:
				if bool(re.match(".(?i)*"+veg+".*",name) and not (name in soups)):
					proteins.append(name);
					break
	for key in mexicanIngredients:
		is_present=False
		for item in ingredientList:
			name = item.get("name");
			if bool(re.match(".(?i)*"+name+".*",str(key))):
				is_present=True
				count+=1
				break
		if(count>=2):
			#Has many mexican ingredients in it so probably mexican even though not categorized as such
			return preperationList
		if (not is_present):
			temp_dict={};
			temp_dict['name']=key;
			holder=mexicanIngredients.get(key);
			splitAmount=holder.split()
			if (len(splitAmount)>1):
				temp_dict['amount']=int(splitAmount[0]);
				if splitAmount[1] in measurements:
					temp_dict['amount_type']=splitAmount[1];
				else:
					i=2
					temp_dict['notes']=splitAmount[1]
					while (i<len(splitAmount)):
						temp_dict['notes']=temp_dict.get('notes')+" "+splitAmount[i];
						i+=1
			else:
				temp_dict['amount']=int(splitAmount[0]);
			ingredientList.append(temp_dict)
	hasBone=False;
	bones=[]
	for protein in proteins:
		if protein in proteinsWithBones:
			hasBone=True;
			bones.append(protein);
	if hasBone:
		deboneStep="Shred the"
		for food in bones:
			deboneStep=deboneStep+ " "+ food;
		deboneStep=deboneStep+" and remove bones."
		preperationList.insert(len(preperationList), deboneStep)
	hasMarinate = False
	for step in preperationList:
		if "marinade" in step or "marinate" in step:
			hasMarinate=True
	if (len(proteins)==0):
		newSteps = "Sprinkle"
		for spice in mexicanIngredients:
			newSteps = newSteps+" "+ spice+",";
		newSteps=newSteps+ " on top of the dish for extra flavor."
		preperationList.insert(len(preperationList), newSteps)
	elif not hasMarinate:
		newSteps = "Marinate"
		for protein in proteins:
			newSteps= newSteps+" "+ protein+",";
		newSteps =newSteps+" in"
		for spice in mexicanIngredients:
			newSteps = newSteps+" "+ spice+",";
		newSteps=newSteps+ " for at least one hour before starting."
		preperationList.insert(3, newSteps)
	else:
		newSteps= "Add to marinade";
		for spice in mexicanIngredients:
			newSteps = newSteps+" "+ spice+",";
		stepCounter=0
		check=True
		for step in preperationList:
			if "marinade" in step or "marinate" in step: 
				findMarinate=step.split(".")
				holder=[]
				j = 0
				
				while j<len(findMarinate):
					#print(check)
					holder.append(findMarinate[j])
					if(check and "marinade" in findMarinate[j] or "marinate" in findMarinate[j]):
						holder.append(newSteps)
						check = False
					j+=1
				holder=" ".join(holder)
				preperationList[stepCounter]=holder
				break
			stepCounter+=1
	isSoup=False
	if "Soup" in foodCategories or "Stew" in foodCategories or "Soups, Stews and Chili" in foodCategories:
		isSoup=True
	#Can't serve soup as tacos
	if not isSoup:
		newPrep= "Serve in"
		for serving in mexicanPreps:
			newPrep = newPrep+" "+ serving;
		newPrep=newPrep+" with";
		for side in mexicanSides:
			newPrep = newPrep+" "+ side+",";
		newPrep=newPrep+" on the side."
	if isSoup:
		newPrep= "Sprinkle"
		for side in mexicanSoupSides:
			newPrep = newPrep+" "+ side+",";
		newPrep=newPrep+" on top."
	preperationList.insert(len(preperationList), newPrep)
	count = 0


	for step in preperationList:
		newItem=step
		for food in nonMexicanIngredinet:
			newItem=newItem.replace(food,"")
			newItem=newItem.replace(food.capitalize(),"")
		for key in mexicanSubsDict:
			newItem=newItem.replace(key, mexicanSubsDict.get(key))
			newItem=newItem.replace(key.capitalize(), mexicanSubsDict.get(key))
		preperationList[count]=newItem
		count+=1
	return(preperationList)
	#print(preperationList)


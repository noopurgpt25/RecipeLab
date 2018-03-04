from constants import *
import re


def makeMexican(ingredientList, preperationList):
	proteins=[]
	count=0
	for key in mexicanIngredients:
		for item in ingredientList:
			name = item.get("name");
			if bool(re.match(".(?i)*"+name+".*",str(key))):
				count+=1
				break
		if(count>=2): #already a mexican dish
			return preperationList
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
			#already mexican
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
	newSteps = "Marinate"
	for protein in proteins:
		newSteps= newSteps+" "+ protein+",";
	newSteps =newSteps+" in"
	for spice in mexicanIngredients:
		newSteps = newSteps+" "+ spice+",";
	newSteps=newSteps+ " for at least one hour before starting."
	newPrep= "Serve in"
	for serving in mexicanPreps:
		newPrep = newPrep+" "+ serving;
	newPrep=newPrep+" with";
	for side in mexicanSides:
		newPrep = newPrep+" "+ side+",";
	newPrep=newPrep+" on the side."
	preperationList.insert(3, newSteps)
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


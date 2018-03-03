from constants import *
import re


def makeMexican(ingredientList, preperationList):
	proteins=[]
	for item in ingredientList:
		present=True;
		name = item.get("name");
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
			if bool(re.match(".(?i)*"+str(item)+".*",str(key))):
				is_present=True
				break
		if (not is_present):
			temp_dict={};
			temp_dict['name']=key;
			holder=mexicanIngredients.get(key);
			splitAmount=holder.split()
			if (len(splitAmount)>1):
				temp_dict['amount']=int(splitAmount[0]);
				temp_dict['amount_type']=splitAmount[1];
			else:
				temp_dict['amount']=int(splitAmount[0]);
			ingredientList.append(temp_dict)
	newSteps = "Marinate"
	for protein in proteins:
		newSteps= newSteps+" "+ protein;
	newSteps =newSteps+" in"
	for spice in mexicanIngredients:
		newSteps = newSteps+" "+ spice;
	newSteps=newSteps+ " for at least one hour before starting."
	preperationList.insert(3, newSteps)
	count = 0
	for step in preperationList:
		newItem=step
		for food in nonMexicanIngredinet:
			newItem=newItem.replace(food,"")
		preperationList[count]=newItem
		count+=1
	return(preperationList)
	#print(preperationList)


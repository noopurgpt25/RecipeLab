from constants import *
import re

def makeSimpler(ingredientList, preperationList, foodCategories):
	if "Desserts" in foodCategories:
		for item in ingredientList:
			name=item.get("name")
			for bake in bakingIngreds:
				if bool(re.match(".(?i)*"+name+".*",bake)):
					ingredientList.remove(item)
		tempDict={}
		tempDict["name"]= "cake mix"
		tempDict["amount"]= 1
		tempDict["amount_type"]= "box"
		ingredientList.append(tempDict)
		stepCounter=0
		check=True
		for item in preperationList:
			findBatter=item.split(".")
			holder=[]
			j = 0
			while j<len(findBatter):
				bakeCount=0
				for bake in bakingIngreds:
					if bake in item and check: 
						bakeCount+=1
						#print (bake)
						#print(findBatter[j])
						if check and bakeCount>=2 and (bake in findBatter[j]):
							holder.append("Pour box of mix in bowl.")
							check = False
							j+=1
							break
				
				holder.append(findBatter[j])

				j+=1
			holder=" ".join(holder)
			preperationList[stepCounter]=holder
					

			stepCounter+=1
		return preperationList
	elif "Pasta and Noodles" in foodCategories:
		for bake in pastaIngreds:
			for item in ingredientList:
				name=item.get("name")
				#if(bool(re.match(".(?i)*"+name+".*","whipping cream"))):
				#	print(name)
				if bool(re.match(".(?i)*"+name+".*",bake)):
					#print(item)
					ingredientList.remove(item)
					#break
			 	
		tempDict={}
		tempDict["name"]= "pasta sauce"
		tempDict["amount"]= 1
		tempDict["amount_type"]= "jar"
		ingredientList.append(tempDict)
		stepCounter=0
		check=True
		for item in preperationList:
			findBatter=item.split(".")
			holder=[]
			j = 0
			while j<len(findBatter):
				bakeCount=0
				for bake in pastaIngreds:
					if bake in item: 
						bakeCount+=1
						#print (bake)
						#print(findBatter[j])
						if check and ((bakeCount>=2) or (bakeCount>=1 and "boil" in item)) and (bake in findBatter[j]):
							holder.append("Pour jar of sauce in pot.")
							#print(holder)
							check = False
							j+=1
							#break
						elif (not check) and ((bakeCount>=2) or (bakeCount>=1 and "boil" in item)) and (bake in findBatter[j]):
							j+=1
						#print(check)
				holder.append(findBatter[j])

				j+=1
			holder=" ".join(holder)
			preperationList[stepCounter]=holder
			stepCounter+=1
		return preperationList
	else:
		return preperationList



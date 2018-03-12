import json
from webScrape import *
from vegitarian import *
from makeHealthy import *
from makeMexican import *
from makeSimple import *
from cookingMethod import *

# testIngredients=scrape_recipe_info(link);
# testSteps=scrape_preperation_info(link);
# testCategories=scrape_categories_info(link);

# user input: link
link = input("Enter an AllRecipes.com link: ")


#link = "https://www.allrecipes.com/recipe/260463/italian-chicken-cacciatore/?internalSource=rotd&referringContentType=home%20page&clickId=cardslot%201";
#link = "https://www.allrecipes.com/recipe/244195/italian-portuguese-meat-loaf-fusion/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%205";
#link = "https://www.allrecipes.com/recipe/262608/cypriot-tahini-pies-with-orange-flavor/?internalSource=staff%20pick&referringContentType=home%20page&clickId=cardslot%2017";
#link = "https://www.allrecipes.com/recipe/246332/carnitas-pressure-cooker/?clickId=right%20rail1&internalSource=rr_feed_recipe_sb&referringId=244195%20referringContentType%3Drecipe"
#link = "https://www.allrecipes.com/recipe/216943/asian-glazed-chicken-thighs/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%205"
#link = "https://www.allrecipes.com/recipe/13087/mulligatawny-soup-i/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202"
#link = "https://www.allrecipes.com/recipe/72508/the-best-vegetarian-chili-in-the-world/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%204"
#link = "https://www.allrecipes.com/recipe/13896/tofu-parmigiana/?internalSource=staff%20pick&referringId=270&referringContentType=recipe%20hub"
#link = "https://www.allrecipes.com/recipe/262234/best-ever-lemon-drizzle-cake/?internalSource=staff%20pick&referringId=276&referringContentType=recipe%20hub"
#link = "https://www.allrecipes.com/recipe/8372/black-magic-cake/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%203"

recipe_dictionary = get_recipe_dictionary(link)

# user input: transformation
while True:
	print("0: View existing recipe")
	print("1: Make recipe vegetarian")
	print("2: Make recipe non-vegetarian")
	print("3: Make recipe healthy")
	print("4: Make recipe unhealthy")
	print("5: Make recipe Mexican-style")
	print("6: Make recipe simpler")
	print("7: Quit")
	inp = int(input("Enter a number: "))

	if inp == 0:
		testSteps = recipe_dictionary['steps']
	elif inp == 1:
		testSteps=makeVegitarian(recipe_dictionary['ingredients'],recipe_dictionary['steps'],recipe_dictionary['categories'])
	elif inp == 2:
		testSteps,testCategories = makeNonVegitarian(recipe_dictionary['ingredients'],recipe_dictionary['steps'],recipe_dictionary['categories'])
	elif inp == 3:
		testSteps= makeHealth(recipe_dictionary['ingredients'],recipe_dictionary['steps'])
	elif inp == 4:
		testSteps= makeUnhealthy(recipe_dictionary['ingredients'],recipe_dictionary['steps'])
	elif inp == 5:
		testSteps = makeMexican(recipe_dictionary['ingredients'],recipe_dictionary['steps'],recipe_dictionary['categories'])
	elif inp == 6:
		testSteps= makeSimpler(recipe_dictionary['ingredients'],recipe_dictionary['steps'], recipe_dictionary['categories'])
	elif inp == 7:
		break
	else:
		print("Invalid input!")

	print(testSteps)

# for thing in testIngredients:
#  	print(thing)
#  	print('\n')

# for thing in testSteps:
# 	print(thing)
# 	print('\n')

# for thing in testCategories:
# 	print(thing)
# 	print('\n')
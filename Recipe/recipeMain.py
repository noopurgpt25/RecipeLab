import json, os, webbrowser
from webScrape import *
from vegitarian import *
from makeHealthy import *
from makeMexican import *
from makeSimple import *
from cookingMethod import *

def showStepsInBrowser(steps, ingredients):
	# steps is a list of strings
	filename = 'recipe.html'
	f = open(filename,'w')

	message = """<html>
	<head>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
	</head>
	<body>
	<div class='container'>
	<h1>Ingredients</h1>
	<ul>"""

	for ingredient in ingredients:
		ingredient_amount = str(ingredient['amount']) if 'amount' in ingredient else ''
		ingredient_amount_type = str(ingredient['amount_type']) if 'amount_type' in ingredient else ''
		ingredient_preparation = str(ingredient['preperation']) if 'preperation' in ingredient else ''
		ingredient_name = str(ingredient['name']) if 'name' in ingredient else ''
		ingredient_notes = str(ingredient['notes']) if 'notes' in ingredient else ''
		message += '<li>' + ingredient_amount + ' '
		if ingredient_amount_type:
			message += ingredient_amount_type + ' of '
		message +=  ingredient_preparation + ' ' + ingredient_name
		if ingredient_notes:
			message += ', note: ' + ingredient['notes']
		message += '</li>'
	message += """</ul>
	<h1>Recipe</h1>
	<ul>
	"""

	for step in steps:
		message += '<li>' + step + '</li>'

	message += """</ul>
	</div>
	</body>
	</html>"""

	f.write(message)
	f.close()

	#Change path to reflect file location
	webbrowser.open('file://' + os.path.realpath(filename))

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


# user input: transformation
while True:
	recipe_dictionary = get_recipe_dictionary(link)
	print("0: View existing recipe")
	print("1: Make recipe vegetarian")
	print("2: Make recipe non-vegetarian")
	print("3: Make recipe healthy")
	print("4: Make recipe unhealthy")
	print("5: Make recipe Mexican-style")
	print("6: Make recipe simpler")
	print("7: Make recipe fry to bake")
	print("8: Make recipe bake to fry")
	print("9: Quit")
	inp = int(input("Enter a number: "))

	if inp == 0:
		steps = recipe_dictionary['steps']
		ingredients = recipe_dictionary['ingredients']
	elif inp == 1:
		steps=makeVegitarian(recipe_dictionary['ingredients'],recipe_dictionary['steps'],recipe_dictionary['categories'])
		ingredients = recipe_dictionary['ingredients']
	elif inp == 2:
		steps,testCategories = makeNonVegitarian(recipe_dictionary['ingredients'],recipe_dictionary['steps'],recipe_dictionary['categories'])
		ingredients = recipe_dictionary['ingredients']
	elif inp == 3:
		steps= makeHealth(recipe_dictionary['ingredients'],recipe_dictionary['steps'])
		ingredients = recipe_dictionary['ingredients']
	elif inp == 4:
		steps= makeUnhealthy(recipe_dictionary['ingredients'],recipe_dictionary['steps'])
		ingredients = recipe_dictionary['ingredients']
	elif inp == 5:
		steps = makeMexican(recipe_dictionary['ingredients'],recipe_dictionary['steps'],recipe_dictionary['categories'])
		ingredients = recipe_dictionary['ingredients']
	elif inp == 6:
		steps= makeSimpler(recipe_dictionary['ingredients'],recipe_dictionary['steps'], recipe_dictionary['categories'])
		ingredients = recipe_dictionary['ingredients']
	elif inp == 7:
		ingredients,steps = fry2bake(recipe_dictionary['ingredients'], recipe_dictionary['steps'])
	elif inp == 8:
		ingredients,steps = bake2fry(recipe_dictionary['ingredients'], recipe_dictionary['steps'])
	elif inp == 9:
		break
	else:
		print("Invalid input!")


	print(ingredients)
	print(steps)
	showStepsInBrowser(steps, ingredients)

# for thing in testIngredients:
#  	print(thing)
#  	print('\n')

# for thing in testSteps:
# 	print(thing)
# 	print('\n')

# for thing in testCategories:
# 	print(thing)
# 	print('\n')
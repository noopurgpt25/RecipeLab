import json
from webScrape import *
from vegitarian import *


testIngredients=scrape_recipe_info()
testSteps=scrape_preperation_info()
#for thing in testIngredients:
#	print(thing.get("name"))
#	print('\n')
testSteps=makeVegitarian(testIngredients,testSteps)
for thing in testIngredients:
	print(thing.get("name"))
	print('\n')

for thing in testSteps:
	print(thing)
	print('\n')
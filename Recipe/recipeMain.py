import json
from webScrape import *
from vegitarian import *
from makeHealthy import *


testIngredients=scrape_recipe_info()
testSteps=scrape_preperation_info()
#for thing in testIngredients:
#	print(thing)
#	print('\n')
#testSteps=makeVegitarian(testIngredients,testSteps)
#for thing in testIngredients:
#	print(thing.get("name"))
#	print('\n')

#for thing in testSteps:
#	print(thing)
#	print('\n')

testSteps= makeHealth(testIngredients,testSteps)
for thing in testIngredients:
	print(thing)
	print('\n')

for thing in testSteps:
	print(thing)
	print('\n')
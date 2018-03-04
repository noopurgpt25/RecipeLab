import json
from webScrape import *
from vegitarian import *
from makeHealthy import *
from makeMexican import *
#link = "https://www.allrecipes.com/recipe/260463/italian-chicken-cacciatore/?internalSource=rotd&referringContentType=home%20page&clickId=cardslot%201";
link = "https://www.allrecipes.com/recipe/244195/italian-portuguese-meat-loaf-fusion/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%205";
#link = "https://www.allrecipes.com/recipe/262608/cypriot-tahini-pies-with-orange-flavor/?internalSource=staff%20pick&referringContentType=home%20page&clickId=cardslot%2017";
#link ="https://www.allrecipes.com/recipe/246332/carnitas-pressure-cooker/?clickId=right%20rail1&internalSource=rr_feed_recipe_sb&referringId=244195%20referringContentType%3Drecipe"
testIngredients=scrape_recipe_info(link)
testSteps=scrape_preperation_info(link)
# for thing in testIngredients:
# 	print(thing)
# 	print('\n')
#testSteps=makeVegitarian(testIngredients,testSteps)
#for thing in testIngredients:
#	print(thing)
#	print('\n')

#for thing in testSteps:
#	print(thing)
#	print('\n')

#testSteps= makeHealth(testIngredients,testSteps)
# for thing in testIngredients:
# 	print(thing)
# 	print('\n')

# for thing in testSteps:
# 	print(thing)
# 	print('\n')


testSteps = makeMexican(testIngredients,testSteps)
for thing in testIngredients:
  	print(thing)
  	print('\n')
for thing in testSteps:
 	print(thing)
 	print('\n')
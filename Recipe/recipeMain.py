import json
from webScrape import *
from vegitarian import *
from makeHealthy import *
from makeMexican import *
from makeSimple import *
from cookingMethod import *

link = "https://www.allrecipes.com/recipe/260463/italian-chicken-cacciatore/?internalSource=rotd&referringContentType=home%20page&clickId=cardslot%201";
#link = "https://www.allrecipes.com/recipe/244195/italian-portuguese-meat-loaf-fusion/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%205";
#link = "https://www.allrecipes.com/recipe/262608/cypriot-tahini-pies-with-orange-flavor/?internalSource=staff%20pick&referringContentType=home%20page&clickId=cardslot%2017";
#link = "https://www.allrecipes.com/recipe/246332/carnitas-pressure-cooker/?clickId=right%20rail1&internalSource=rr_feed_recipe_sb&referringId=244195%20referringContentType%3Drecipe"
#link = "https://www.allrecipes.com/recipe/216943/asian-glazed-chicken-thighs/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%205"
#link = "https://www.allrecipes.com/recipe/13087/mulligatawny-soup-i/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202"
#link = "https://www.allrecipes.com/recipe/72508/the-best-vegetarian-chili-in-the-world/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%204"
#link = "https://www.allrecipes.com/recipe/13896/tofu-parmigiana/?internalSource=staff%20pick&referringId=270&referringContentType=recipe%20hub"
#link = "https://www.allrecipes.com/recipe/262234/best-ever-lemon-drizzle-cake/?internalSource=staff%20pick&referringId=276&referringContentType=recipe%20hub"
#link = "https://www.allrecipes.com/recipe/8372/black-magic-cake/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%203"
link = "https://www.allrecipes.com/recipe/11815/penne-with-spicy-vodka-tomato-cream-sauce/?internalSource=hub%20recipe&referringId=17245&referringContentType=recipe%20hub"

testIngredients=scrape_recipe_info(link);
testSteps=scrape_preperation_info(link);
testCategories=scrape_categories_info(link);

#testSteps = makeMexican(testIngredients,testSteps,testCategories)
#testSteps,testCategories = makeNonVegitarian(testIngredients,testSteps,testCategories)
#testSteps=makeVegitarian(testIngredients,testSteps,testCategories)
#testSteps= makeHealth(testIngredients,testSteps)
#testSteps= makeUnhealthy(testIngredients,testSteps)
# testSteps= makeSimpler(testIngredients,testSteps, testCategories)
testSteps= fry2bake(testIngredients, testSteps)


for thing in testIngredients:
 	print(thing)
 	print('\n')

for thing in testSteps:
	print(thing)
	print('\n')

for thing in testCategories:
	print(thing)
	print('\n')

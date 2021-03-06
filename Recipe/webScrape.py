import json
import re
import bs4
from bs4 import BeautifulSoup
import requests
from constants import *
import re
# Web Scraping

# Scraping Categories

def scrape_recipe_info(link):
    res = requests.get(link)
    #res = requests.get("https://www.allrecipes.com/recipe/244195/italian-portuguese-meat-loaf-fusion/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%205")
    #res = requests.get("https://www.allrecipes.com/recipe/262608/cypriot-tahini-pies-with-orange-flavor/?internalSource=staff%20pick&referringContentType=home%20page&clickId=cardslot%2017")
    content = res.content
    soup = BeautifulSoup(content, 'lxml')
    counter=1
    ingredients = []
    while (True):
        element = soup.find(id="lst_ingredients_"+str(counter))
        if element !=None:
            for li in element:
                if((isinstance(li,bs4.element.Tag))):
                    ingredients.append(li.find("span").get_text())
            counter+=1
        else:
            break
    ignoreLastIngreedient = ingredients[:-1]
    ingredientDiction=[]
    for tempIng in ignoreLastIngreedient:
        temp_dict={}
        splitString=tempIng.split()
        if (splitString[0][0].isdigit()):
            if (splitString[1][0].isdigit()):
                holder= splitString[1].split("/");
                temp_num= float(holder[0])/float(holder[1]);
                temp_dict['amount']=int(splitString[0])+ temp_num;
                splitString.remove(splitString[0]);
            else:
                holder= splitString[0].split("/");
                if (len(holder)>1):
                    temp_dict['amount']=float(holder[0])/float(holder[1]);
                else:
                    temp_dict['amount']=int(holder[0]);
            if (splitString[1][0]=="("):
                newMes=splitString[1]
                i=0
                splitString.remove(splitString[0])
                splitString.remove(splitString[0])
                while (True):
                    if(splitString[i][-1]==")"):
                        newMes=newMes+" "+splitString[i]
                        splitString.remove(splitString[i])
                        if splitString[i] in measurements:
                            temp_dict['amount_type']=newMes+" "+splitString[i]
                            splitString.remove(splitString[i])
                        else:
                            temp_dict['amount_type']=newMes
                        break
                    else:
                        newMes=newMes+" "+splitString[i]
                        splitString.remove(splitString[i])
            elif (splitString[1] in measurements):
                newMes=splitString[1]
                splitString.remove(splitString[0])
                splitString.remove(splitString[0])
                temp_dict['amount_type']=newMes
            else:
                splitString.remove(splitString[0])
        else:
            for item in splitString:
                if item in measurements:
                    if item=="a":
                        temp_dict['amount']=1
                        splitString.remove(item)
                    elif item=="taste":
                        temp_dict['amount_type']="to taste"
                        splitString.remove(item)
                        splitString.remove("to")
        for item in splitString:
            temp=item.replace(",","")
            if temp in preperation:
                temp_dict['preperation']=temp
                splitString.remove(item)
        name=" ".join(splitString)
        nameSplit=name.split(',')
        temp_dict['name']=nameSplit[0]
        if(len(nameSplit)>1):
            if (len(nameSplit[1])!=0):
                temp_dict['notes']=nameSplit[1]

        ingredientDiction.append(temp_dict)
    return ingredientDiction

def scrape_preperation_info(link):
    res = requests.get(link)
    #res = requests.get("https://www.allrecipes.com/recipe/244195/italian-portuguese-meat-loaf-fusion/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%205")
    #res = requests.get("https://www.allrecipes.com/recipe/262608/cypriot-tahini-pies-with-orange-flavor/?internalSource=staff%20pick&referringContentType=home%20page&clickId=cardslot%2017")
    content = res.content
    soup = BeautifulSoup(content, 'lxml')
    preperation = []
    element = soup.find("div", {"class": "directions--section__steps"})
    count =1
    for item in element:
        if((isinstance(item,bs4.element.Tag))):
            temp=item.get_text();
            temp = temp.splitlines()
            for step in temp:
                if(len(step)>0):
                    if(count==1):
                        preperation.append("Preperation Time: "+ step[4:])
                        count+=1
                    elif(count==2):
                        preperation.append("Cooking Time: "+ step[4:])
                        count+=1
                    elif(count==3):
                        preperation.append("Total Time: "+ step[8:])
                        count+=1
                    else:
                        preperation.append(step)
    return preperation


def scrape_categories_info(link):
    res = requests.get(link)
    content = res.content
    soup = BeautifulSoup(content, 'lxml')
    element = soup.find_all("meta",  itemprop="recipeCategory")
    # element =element.find_all(text="content")
    categories=[]
    for item in element:
        categories.append(item["content"])
    return(categories)

def scrape_tools_info(preparation_steps):
    # input: list of steps (strings) output: list of strings (tools)
    tools_list = []
    for step in preparation_steps:
        for tool in tools:
            if bool(re.match('.(?i)*'+tool+'.*',step)):
                tools_list.append(tool)
    return tools_list

def scrape_methods_info(preparation_steps):
    # input: list of steps (strings) output: list of strings (tools)
    methods_list = []
    for step in preparation_steps:
        for method in cookingMethods:
            if bool(re.match('.(?i)*'+method+'.*',step)):
                methods_list.append(method)
    # get ride of duplicates
    methods_list = list(set([m.lower() for m in methods_list]))
    return methods_list

def get_recipe_dictionary(link):
    d = {}
    d['ingredients'] = scrape_recipe_info(link)
    d['steps'] = scrape_preperation_info(link)
    d['categories'] = scrape_categories_info(link)
    d['methods'] = scrape_methods_info(d['steps'])
    d['tools'] = scrape_tools_info(d['steps'])
    return d
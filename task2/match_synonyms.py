import pandas as pd
import json
import numpy as np
import Levenshtein as lev
import ast
import nltk


# Ingredio vars
data = []
pmid_data = []

def Ingredio_articles():   
    #Load Json to list
    with open('pmid_final.json') as f:
        for line in f:
            data.append(json.loads(line))
            
    #Retrieve PMID and meta data and add them to list
    for inner_l in data:
        for item in inner_l['pmid']:
            pmid_data.append(item)
    
    ingredioDF = pd.DataFrame(pmid_data)
    #Drop useless columns
    ingredioDF.drop(['Journal'], axis = 1,inplace = True) 
    ingredioDF['Abstract'].replace('', np.nan, inplace=True)
    ingredioDF = ingredioDF[pd.notnull(ingredioDF['Abstract'])]
    ingredioDF['Abstract'] = ingredioDF['Article'] + ingredioDF['Abstract']
    ingredioDF.drop(['Article'], axis = 1,inplace = True) 
    ingredioDF.dropna(how='any', inplace=True)
    return ingredioDF

ingredioDF = Ingredio_articles()


#Load Ingredio DB
def ingredio_DB():
    with open('D:/Downloads/Prototype/new_with_g.json', encoding="utf8") as json_file:
        data = json.load(json_file)
    json_file.close()
    ingredio_dict = data['Ingredients_withFoods']
    return ingredio_dict

ingredio_dict = ingredio_DB()

matchinr = pd.DataFrame(ingredio_dict)

for index, row in ingredioDF.iterrows():
    for matchindex, matchrow in matchinr.iterrows():
        if row['Pubchem_ID'] == matchrow['pubchemId']:
            ingredioDF.at[index,'syns'] = matchrow['compName']
            print(f'evrethin {index},{matchindex}')

ingredioDF.to_csv('compoundDF.csv')
import pandas as pd
import json
import numpy as np
import Levenshtein as lev
import ast
import nltk

#Load the dataframe
def load_DB(path):
    df = pd.read_csv(path)
    df.drop(['Unnamed: 0','Pubchem_ID'], axis = 1,inplace = True)
    df = df[df['syns'].notna()]
    df.dropna(how='any', inplace=True)
    df.syns = df.syns.apply(lambda s: list(ast.literal_eval(s)))
    return df


path = 'D:/Downloads/compoundDF.csv'
ingredioDF = load_DB(path)

#Tokenize Abstracts to sentences
sentences = []
for row in ingredioDF.itertuples():
    for sentence in nltk.sent_tokenize(row[2]):
        d = {} 
        d['PMID'] = row[1]
        d['Abstract'] = sentence
        d['DOI'] = row[3]
        d['syns'] = row[4]
        sentences.append(d)
ingredioDF = pd.DataFrame(sentences)

#Match compounds for each sentence with the synonyms from ingredio
def match_syns(df):
    for index, row in df.iterrows():
        comp_list = []
        comp_index_list = []
        found = False
        syns =  df['syns'][index]
        for comp_index,word in enumerate(df['Abstract'][index].split()):
            for comp in syns:
                Ratio = lev.ratio(comp,word.lower())
                if Ratio > 0.7:
                    comp_list.append(comp)
                    comp_index_list.append(comp_index)
                    found = True
                    break
        if comp_list:
            df.at[index,'compound'] = comp_list
            df.at[index,'comp_index'] = comp_index_list
        print(index)
        
    df.dropna(how='any', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df
    
ingredioDF['compound'] = pd.Series().astype(object)
ingredioDF['comp_index'] = pd.Series().astype(object)
ingredioDF = match_syns(ingredioDF)

#Create a list of dictionaries with each word/pos tag and target
dict_list = []
for index, row in ingredioDF.iterrows():
    tokens = nltk.word_tokenize(row['Abstract'])
    tags = nltk.pos_tag(tokens)
    syns =  ingredioDF['syns'][index]
    for tag in tags:      
        test_dict = {}
        found = False
        test_dict['PMID'] = row['PMID']
        test_dict['Word'] = tag[0]
        test_dict['POS'] = tag[1]
        for comp in syns:
            Ratio = lev.ratio(comp,tag[0].lower())
            if Ratio > 0.7:
                x = tag[0],tag[1],Ratio,1
                found = True
        if found:
            test_dict['Tag'] = 1
        else:
            test_dict['Tag'] = 0
        dict_list.append(test_dict)
    print(index)
    
posDF = pd.DataFrame(dict_list)
    
ingredioDF.drop(['DOI', 'syns'], axis=1, inplace=True)
df1 = posDF[posDF.isna().any(axis=1)]

posDF.to_csv('compoundDF_BERTReady.csv')
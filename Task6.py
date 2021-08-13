import json
from bs4 import BeautifulSoup
with open ("Task5.json","r")as f:
    data=json.load(f)
def analyse_movie_language(data):
    dict1={}
    for i in data:
        if "language" in i:
            language=i["language"]
            if language not in dict1:
                language=i["language"]
                dict1[language]=1
            else:
                dict1[language]+=1
        else:
            continue
    with open("Task6.json","w")as f:
        json.dump(dict1,f,indent=4)
analyse_movie_language(data)
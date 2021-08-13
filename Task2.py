import requests
from bs4 import BeautifulSoup
# from pprint import pprint
import json
file=open("Task1.json")
movies=json.load(file)
def group_by_year():
    dic={}
    for i in movies:
        movie_list=[]
        year=i["year"]
        if year not in dic:
            for j in movies:
                if year==j["year"]:
                    movie_list.append(j)
                    # pprint(movie_list)
            dic[year]=movie_list
    with open("Task2.json","w+") as file1:
        json.dump(dic,file1,indent=4)
        b=json.dumps(dic)
        # print(type(b))
        # print(b)
group_by_year()


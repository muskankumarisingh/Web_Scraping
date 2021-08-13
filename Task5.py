import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Task1 import movie_data
from Task4 import scrape_movie_details
movie=movie_data()
def get_movie_list_details():
    movie_list=[]
    for i in movie:
        x=i["movie_url"]
        y=scrape_movie_details(i["movie_name"],x)
        movie_list.append(y)
        pprint(movie_list)
    with open("Task5.json","w+") as file5:
        json.dump(movie_list,file5,indent=4)
get_movie_list_details()
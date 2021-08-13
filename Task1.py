import requests
import json
from bs4 import BeautifulSoup
# from pprint import pprint
all_movie_link=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
data=BeautifulSoup(all_movie_link.text,"html.parser")
def movie_data():
    list=[]
    div=data.find("div",class_="body_main container")
    # print(div)
    table=div.find("table",class_="table")
    # print(table)
    tablerow=table.find_all('tr')
    for i in tablerow:
        dic={}
        alltds=i.find_all('td')
        # print(alltds)
        for j in alltds:
            rank=i.find('td',class_="bold").get_text()[:-1]
            dic["rank"]=int(rank)
            # print(rank)
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            dic["rating"]=int(rating)
            # print(rating)
            review=i.find("td",class_="right hidden-xs").get_text()
            dic["review"]=int(review)
            # print(review)
            movie_name=i.find("a",class_="unstyled articleLink")["href"][3:]
            dic["movie_name"]=movie_name
            # print(movie_name)
            movie_url=i.find("a",class_="unstyled articleLink")["href"]
            movie_link=("https://www.rottentomatoes.com/")+movie_url
            dic["movie_url"]=movie_link
            # print(movie_link)
            year=i.find("a",class_="unstyled articleLink").text
            dic["year"]=int(year[-5:-1])
            # print(dic)
        list.append(dic.copy())
        if {} in list:
            list.remove({})
        # pprint(list)
    with open ("Task1.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
movie_data()        


        




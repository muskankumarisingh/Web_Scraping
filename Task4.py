import requests
from bs4 import BeautifulSoup
import json
# from pprint import pprint
movie_url = "https://www.rottentomatoes.com//m/how_to_train_your_dragon"
movie_name = "how_to_train_your_dragon"
def scrape_movie_details(movie_name,movie_url):
    url = requests.get(movie_url)
    data = BeautifulSoup(url.text,"html.parser")
    main_Div = data.find_all("li",class_ = "meta-row clearfix")
    dict1 = {}
    for i in main_Div:
        a = i.text
        b = a.split(":")
        if "\nRating" in b:
            dict1["Rating"] =  b[1].replace("\n","").strip()
        elif "\nGenre" in b:
            c = b[1].replace("\n                        ","").strip()
            list1 = []
            s = ""
            for i in c:
                if i == ",":
                    list1.append(s)
                    s = ""
                else:
                    s += i                
            dict1["Genre"] = list1
            #print(list1)
        elif "\nOriginal Language" in b:
            dict1["language"] = b[1].replace("\n","").strip()
        elif "\nDirector" in b:
            i = 0
            list2 = []
            while i < len(b):
                if i == 0:
                    i += 1
                    continue
                list2.append(b[i].replace("\n",""))
                i += 1
            # dict1["director"] = list2
            s=""
            for i in list2:
                for j in i:
                    if j==" ":
                        continue
                    else:
                        s+=j
            list5=s.split(",")
            dict1["director"] = list5
        elif "\nProducer" in b:
            i = 0
            list3 = []
            while i < len(b):
                if i == 0:
                    i += 1
                    continue
                list3.append(b[i].replace("\n                        ","").strip())
                i += 1
            list4=[]
            str1=""
            for k in list3:
                for l in k:
                    if l==" ":
                        continue
                    else:
                        str1+=l
            list4=str1.split(",")
            dict1["Producer"]=list4
            # list4=[]
            # for i in list3:
            #     a=i.split("\n")   
            #     for j in a:
            #         if j=="":
            #             continue
            #         else:
            #             list4.append(j)

        elif "\nRuntime" in b:
            s = b[1].replace("\n","").strip()
            hour_formula = int(s[0])*60
            i = 0
            j = " "
            while i < len(s):
                if s[i] == "h" or s[i] == "m"  or s[i] == " " or i == 0 or s[i] == "M":
                    i += 1
                    continue
                else:
                    j += s[i]
                    i += 1
                hour_formula += int(j)   
            dict1["Runtime"] = hour_formula
            dict1["movie_name"] = movie_name                   
    with open("Task4.json","w+") as file4:
            json.dump(dict1,file4,indent = 4)
    return  dict1

scrape_movie_details("how_to_train_your_dragon","https://www.rottentomatoes.com//m/how_to_train_your_dragon")
# pprint(one_movie_data)




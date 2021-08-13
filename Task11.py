import json
with open("Task5.json","r")as file:
    data=json.load(file)
def analyse_movie_genre():
    dict1={}
    for i in data:
        dic={}
        c=0
        if "Genre" in i:
            for j in i["Genre"]:
                genre=j
                for g in data:
                    if "Genre" in g:
                        for gen in g["Genre"]:
                            if genre==gen: 
                                c+=1 
            dic[genre]=c
            dict1.update(dic)
    with open("Task11.json","w")as f:
        json.dump(dict1,f,indent=4)
analyse_movie_genre()
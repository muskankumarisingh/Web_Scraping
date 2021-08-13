import requests
import json
from bs4 import BeautifulSoup
# from pprint import pprint
file=open("Task1.json")
movies=json.load(file)
# pprint(movies)
decades={"1937":[],"1947":[],"1957":[],"1967":[],"1977":[],"1987":[],"1997":[],"2007":[],"2017":[],"2027":[]}
def group_by_decade(movies):
    for index in movies:
        if index["year"]>=1937 and index["year"]<=1947:
            decades["1937"].append(index)
        elif index["year"]>=1947 and index["year"]<=1957:
            decades["1947"].append(index)
        elif index["year"]>=1957 and index["year"]<=1967:
            decades["1957"].append(index)
        elif index["year"]>=1967 and index["year"]<=1977:
            decades["1967"].append(index)
        elif index["year"]>=1977 and index["year"]<=1987:
            decades["1977"].append(index)
        elif index["year"]>=1987 and index["year"]<=1997:
            decades["1987"].append(index)
        elif index["year"]>=1997 and index["year"]<=2007:
            decades["1997"].append(index)
        elif index["year"]>=2007 and index["year"]<=2017:
            decades["2007"].append(index)
        elif index["year"]>=2017 and index["year"]<=2027:
            decades["2017"].append(index)
        with open("Task3.json","w+") as file3:
            json.dump(decades,file3,indent=4)
            a=json.dumps(decades)
            # pprint(a)
group_by_decade(movies)




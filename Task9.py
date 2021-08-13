import requests
import os
import time
import random
from Task1 import movie_data
movie=movie_data()
def get_movie_list_details():
    movie_list=[]
    for index in movie:
        random_sleep=random.randint(1,5)
        path="/home/dell45/Desktop/WEB_SCRAPING/All_file/"+index["movie_name"]+".text"
        if os.path.exists(path):
            pass
        else:
            time.sleep(random_sleep)
            create=open("/home/dell45/Desktop/WEB_SCRAPING/All_file/"+index["movie_name"]+".text","w")
            url=requests.get(index["movie_url"])
            create1=create.write(url.text)
            create.close()
get_movie_list_details()

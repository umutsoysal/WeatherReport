import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import helpermethods

from datetime import datetime



def download(date):
    response = urlopen('https://www.glerl.noaa.gov/metdata/chi/2022/'+date+'.04t.txt')
    data = response.read()
    filename = date+".txt"
    file_ = open(filename, 'wb')
    file_.write(data)
    file_.close()



year = "2022" 
for i in range(1,366):
    #print(i)
    day_num=str(i)
    day_num.rjust(3 + len(day_num), '0')  
    res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%Y%m%d")
    #print("Resolved date : " + str(res))
    download(str(res))
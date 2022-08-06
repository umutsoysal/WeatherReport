
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

url="https://www.glerl.noaa.gov/metdata/plot_3hr.php?site=chi&units=e#metdata"
html_content = requests.get(url)

# Parse the html content
soup = BeautifulSoup(html_content.content, "html.parser")

table = soup.find("pre").contents[0]
data = str(table.string)
df = pd.DataFrame([x.split(';') for x in data.split('\n')[1:]], columns=[x for x in data.split('\n')[0].split(';')])
#print(df)
df1=df[3:]
df1.columns = ['raw']
df1=df1.raw.str.split(expand=True,)
df1.columns = ['Date','CDT','WindSpeed(kts)','WindGust(kts)','WindDir(ang)','AirTemp(F)','DewPoint(F)','RelHum(%)']
df1.drop(df1.tail(1).index,inplace=True) # drop last n rows
df1.reset_index(drop=True)

df1[["WindSpeed(kts)", "WindGust(kts)",'WindDir(ang)']] = df1[["WindSpeed(kts)", "WindGust(kts)",'WindDir(ang)']].apply(pd.to_numeric)


ans=df1["WindSpeed(kts)"][3]

print(ans)
from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd


url2 = 'https://www.map-testing.com/map-search/?start=3&searchOptions=AllResults'
urlh2 = requests.get(url2)
info2 = urlh2.text
#print(info2)
soup = BeautifulSoup(info2, 'html.parser')
toilets = soup.find_all('div', attrs= {'class' : 'search-result'})
datalist = []

for s in toilets[0].stripped_strings:
    datalist.append(s)
dict = {}
count = 0
for info in datalist[:9]:
    if count == 0:
        dict[info] = datalist[count + 1]
        count += 1
    elif (count % 2) == 1:
        count += 1
        continue
    elif (count % 2) == 0:
        dict[info] = datalist[count + 1]
        count += 1
specs = datalist[11:22]
dict['Specifications'] = specs
df = pd.DataFrame(dict)
print(df)
#df.to_excel('MaPTesting.xlsx')

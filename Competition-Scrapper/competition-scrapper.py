import requests
from bs4 import BeautifulSoup
import json

url = r"https://clist.by/"

data = {}
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
i = 0
for event in soup.find_all('a',attrs = {"class":'data-ace'}):
    data[i+1] = event.attrs.get("data-ace", None).strip()
    i += 1
d = json.dumps(data,indent=4)

with open('data.json', 'w') as outfile:
    outfile.write(d)
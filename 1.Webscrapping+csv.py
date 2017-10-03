import urllib.request
from bs4 import BeautifulSoup
import csv

url_address = 'https://www.babynamesdirect.com/blender/indian/girl/rahul-manisha-d'

url_open = urllib.request.urlopen(url_address)
snippet = url_open.read()
url_open.close()

soup = BeautifulSoup(snippet, 'html.parser')

filename = "baby_names.csv"
file = open(filename, "w")
headers = "Name, Gender/n"
file.write(headers)

for sp in soup.findAll("u", attrs={"class":"m"}):
    sp1 = sp.contents[0]
    print(sp1)
for sp in soup.findAll("u", attrs={"class":"f"}):
    sp2 = sp.contents[0]
    print(sp2)
    file.write(sp1 + "," +sp2)
file.close()

    
    



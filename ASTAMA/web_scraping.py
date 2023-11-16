import requests
r=requests.get(https://geeksfor geeks.org/python-programming-language/')
print(r.url)
print(r.status_code)
from bs4 import BeautifulSoup
r=requests.get(https://geeksfor geeks.org/python-programming-language/')
print(r)
soup=BeautifulSoup(r.content,'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)
s=soup.find('div',class_='entry-content')
lines=s.find_all('p')
for line in lines:
  print(line.text)
                

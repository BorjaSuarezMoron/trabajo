import requests
from bs4 import BeautifulSoup

url= "http://www.example.com/"
r= requests.get(url)
html= r.text
soup= BeautifulSoup(html, 'html.parser')
print soup.find('h1')
import requests
from bs4 import BeautifulSoup

url= "https://es.wikipedia.org/wiki/Holanda"
r= requests.get(url)
html= r.text
soup = BeautifulSoup(html, 'html.parser')
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images)
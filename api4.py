import requests

url="en.wikipedia.org/wiki/Main_Page"
r=requests.get("http://www.example.com/", headers={"content-type":"head"})

print r.text
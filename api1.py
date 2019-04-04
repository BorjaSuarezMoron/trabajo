import requests


if __name__ =='__main__':
    url= "https://es.wikipedia.org/wiki/Wikipedia:Portada"
    r= requests.get(url)
    if r.status_code == 200:
        header=r.headers
        server= header['Server']
        print(server)

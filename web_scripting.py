from bs4 import BeautifulSoup  # HTML data structure
import requests
import scrapy

nameFile="index.html"
f =open(nameFile,"w")
url = 'https://www.base64decode.org/'
r = requests.get(url)


text="Y2lhbwo=" #ciao
format={'input':text}
r=requests.post(url=url,data=format)
f.write(r.text)
f.close()




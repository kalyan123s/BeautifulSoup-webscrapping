from bs4 import BeautifulSoup
import requests

# with open("html_read.html",'r') as html_read:
#     content=html_read.read()
#     print(content)

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
soup=BeautifulSoup(html_text.text,'lxml')
jobs=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
print(jobs) 
#My name is Arif Rahman Hakim
#This Code will give output packages from https://booksc.org/
#import librarry i need
import requests
from bs4 import BeautifulSoup
#make var for url
url = 'https://booksc.org/s'
#will get input what want to search
a = input("Please enter what you want to search: ")
#in thsi part will sent request to server
reg = requests.get(url + '/' + a)
#result will sotage in result variable
result = reg.content
#using soup to desirve html
soup = BeautifulSoup(result, 'html.parser')
#this two line for grep tiltle Article and author
title = soup.findAll('h3', attrs={'itemprop':'name'})
author = soup.findAll('div', attrs={'class':'authors'})
if not title:
    print("Article not found")
#this is looping for get outpur
for i in range(len(title)):
    print("{0}.{1}\n  Author: {2}\n".format(i ++ 1, title[i].text.strip(),author[i].text.strip()))



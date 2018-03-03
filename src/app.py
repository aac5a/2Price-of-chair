__author__ = 'piotr'

import requests
from bs4 import BeautifulSoup

request = requests.get('https://abc-rc.pl/propeller-8045x2-DJI-black')
content = request.content
print(content)
soup = BeautifulSoup(content, 'html.parser')
element = soup.find('div', {'class': 'view_price'})
# <b class="my_shop_price ajax-price" data-shopprice="158.67" id="unit_price" data-key="604500#21" data-orgp="89.99" style="visibility: visible;">$89.<i>99</i></b>
# https://abc-rc.pl/propeller-8045x2-DJI-black
#print(element)
#print(element.text.strip())



elem1 = soup.select('div[class="view_price"] span[class="price_1"]')
print(elem1)
elem2 = soup.find('span', {'class':'price_1'})
print(elem2)
elem3 = soup.find_all('span', {'class':'price_1'})
print(elem3[1])
print(elem1[0].getText())
print(elem1[0].attrs)
print(elem1[0].get('class'))
#print(soup.find())
"""https://www.facebook.com/tombakfanclub/
try:
    request.raise_for_status()
except:
    print("dupaaaa!!")

soup = BeautifulSoup(request.content, 'html.parser')
cena = soup.find("span", {'itemprop':'price'})
print(cena.att)"""

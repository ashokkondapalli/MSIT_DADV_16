# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 18:49:47 2015

@author: Poonam Goje
"""

from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

page = requests.get(url)
tree = html.fromstring(page.content)

list=tree.xpath('//a[@rel="nofollow"][@class="external text"]/text()')
print list[1]

i=0
nlist=[]
while(i<len(list)-1):
    nlist.append(list[i])
    i=i+2


for i in range(0,2):
   #print nlist[i]
   str=""+nlist[i]
   page = requests.get('http://finance.yahoo.com/q/hp?s='+str+'+Historical+Prices')
   #print page
   tree = html.fromstring(page.content)
   low_price = tree.xpath('//td[@class="yfnc_tabledata1"][@align="right"]/text()')
   k=0
   low=[]
   while(k<len(low_price)):
      if(k+4>=len(low_price)):
          break
      low.append(low_price[k+4])
      k=k+7
   print (nlist[i]+" is its closing prices list")
   print(low)
    

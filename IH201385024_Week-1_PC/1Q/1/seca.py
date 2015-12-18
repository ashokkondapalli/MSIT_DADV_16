# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 14:11:23 2015

@author: alluriharitha
"""
import sys
import urllib
import requests
from lxml import html
 
def get(url):
    '''Retrives a URL'''
    sys.stderr.write(url + '\n')
    return urllib.urlopen(url).read()
 
def safe(line):
    '''Strips out all unsafe / non-ASCII characters'''
    return ''.join(char for char in line if 32 <= ord(char) < 128)
 
# The output will be written to a CSV file with these fields
 
# Download the main URL
url = 'http://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType=NIFTY%20500&fromDate=09-12-2014&toDate=05-11-2015'
page = requests.get(url)
tree = html.fromstring(page.content)
list=tree.xpath('//div/text()')
#print len(list)
newlist=list[0].split(":")
print len(newlist)
list1=newlist[1:]
print len(list1)
import csv
with open('hist1.csv', 'wb') as f:
    fieldnames=['Date','Open','High','Low','Close','Shares Traded', 'Turnover']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(list1)-1):
        temp=list1[i].split(",")
        writer.writerow({'Date':temp[0],'Open':temp[1],'High':temp[2],'Low':temp[3],'Close':temp[4],'Shares Traded':temp[5],'Turnover':temp[6]})


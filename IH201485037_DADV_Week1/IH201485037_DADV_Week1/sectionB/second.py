import csv
from bs4 import BeautifulSoup
import urllib
import urllib.request
import os


symbols = []

page = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
soup = BeautifulSoup(page)


table = soup.find('table', {'class': 'wikitable sortable'})
for row in table.findAll('tr'):
    col = row.findAll('td')
    if len(col) > 0:
        symbols.append(str(col[0].string.strip()))



for i in range(0,499):
    page1 = urllib.request.urlopen("http://finance.yahoo.com/q/hp?s="+symbols[i]+"Historical+Prices")
    url = ("http://real-chart.finance.yahoo.com/table.csv?s="+symbols[i]+"&d=11&e=9&f=2015&g=d&a=10&b=18&c=1999&ignore=.csv")
    response = urllib.request.urlopen(url)
    html = response.read()
    filename = str(i)+"stfile"+".csv"
    with open(filename, 'wb') as f:
        f.write(html)
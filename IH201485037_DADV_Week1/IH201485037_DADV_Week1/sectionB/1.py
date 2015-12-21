from bs4 import BeautifulSoup
from lxml import html
import urllib
import urllib.request
symbols = []

page = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
soup = BeautifulSoup(page)


table = soup.find('table', {'class': 'wikitable sortable'})
for row in table.findAll('tr'):
    col = row.findAll('td')
    if len(col) > 0:
        symbols.append(str(col[0].string.strip()))
for i in symbols:
    page = requests.get("http://finance.yahoo.com/q/hp?s="+str(i)+"+Historical+Prices")
    tree = html.fromstring(page.content)
    low_price = tree.xpath('//td[@class="yfnc_tabledata1"]/text()')
    print(low_price)
    i=0
    low=[]
    while(i<len(low_price)):
        if(i+4>=len(low_price)):
            break
        low.append(low_price[i+4])

        i=i+7

    print(low)

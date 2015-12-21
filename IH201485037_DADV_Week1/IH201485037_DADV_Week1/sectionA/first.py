

from lxml import html
import requests
import csv

page = requests.get('http://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType=NIFTY%20500&fromDate=09-12-2014&toDate=05-11-2015')
tree = html.fromstring(page.content)

dates = tree.xpath('//nobr/text()')
values=tree.xpath('//td[@class="number"]/text()')

opens=[]
high=[]
low=[]
close=[]
shares=[]
turnover=[]
k=0
while(k<len(values)):
    opens.append(values[k])
    high.append(values[k+1])
    low.append(values[k+2])
    close.append(values[k+3])
    shares.append(values[k+4])
    turnover.append(values[k+5])
    k=k+6
f1= open('E:\dadv\IH201485037_DADV_Week1\sectionA\out.csv', "wt")
writer = csv.writer(f1, delimiter=',')

final=[]
i=0
print(len(opens))
while(i<len(dates)):
    data1=[]
    data1.append(dates[i])
    #print(i)
    data1.append(opens[i])
    data1.append(high[i])
    data1.append(low[i])
    data1.append(close[i])
    data1.append(shares[i])
    data1.append(turnover[i])
    final.append(data1)
    i=i+1

i=0
while(i<len(final)):
    writer.writerow(final[i])
    i=i+1

f1.close()


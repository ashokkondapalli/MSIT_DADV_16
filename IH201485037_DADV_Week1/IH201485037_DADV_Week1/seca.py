import csv
import urllib2

url = 'http://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType=NIFTY%20500&fromDate=09-12-2014&toDate=05-11-2015'
response = urllib2.urlopen(url)
cr = csv.reader(response)
f = open("historical.csv","w");
for row in cr:
    f.write(row)
f.close()    
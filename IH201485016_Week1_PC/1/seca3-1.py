# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 18:09:18 2015

@author: Anvesh
"""


from lxml import etree

f = open("company.csv","r")
s = f.read()
parser = etree.HTMLParser()
tree = etree.fromstring(s, parser)
results = tree.xpath('//tr/td[position()=2]')
f = open("symbols.csv","w")
#print 'Column 2\n========'
for r in results:
    t = r.text+'\n'
    f.write(t)
f.close()
##text = urllib2.urlopen(url).read()

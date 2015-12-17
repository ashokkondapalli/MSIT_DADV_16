# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 14:47:35 2015

@author: Anvesh
"""

import re
file1=open('pc11.csv','r')
s=file1.readlines()
s1=s[5:106]
date=[]
op=[]
high=[]
low=[]
close=[]
shares=[]
turnover=[]
date2=[]
#Task2
f = open('hist.csv','w')
for i in range(len(s1)-1):
    m=s1[i].split("\t")
    #print m
    date.append(m[0])
    op.append(m[1])
    high.append(m[2])
    low.append(m[3])
    close.append(m[4])
    shares.append(m[5])
    turnover.append(m[6])
    date2.append((re.search(r'([0-3][0-9]-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-(2013|2014|2015))',m[0])).group(0))
f.write("date open high low close share turnover\n")
for i in range(len(date)):
    if(date[i]==date2[i]):
        f.write(date[i] +" "+op[i]+" "+high[i]+" "+low[i]+" "+close[i]+" "+shares[i]+" "+turnover[i] )
f.close()   
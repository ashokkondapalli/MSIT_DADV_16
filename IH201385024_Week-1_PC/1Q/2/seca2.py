# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 14:47:35 2015

@author: alluriharitha
"""

import re
file1=open('historical.csv','r')
s=file1.readlines()
s1=s[5:106]
date1=[]
open1=[]
high1=[]
low1=[]
close1=[]
shares=[]
turnover=[]
date2=[]
#Task2
f = open('newhist.csv','w')
for i in range(len(s1)-1):
    m=s1[i].split("\t")
    #print m
    date1.append(m[0])
    open1.append(m[1])
    high1.append(m[2])
    low1.append(m[3])
    close1.append(m[4])
    shares.append(m[5])
    turnover.append(m[6])
    date2.append((re.search(r'([0-3][0-9]-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-(2013|2014|2015))',m[0])).group(0))
f.write("date open high low close share turnover\n")
for i in range(len(date1)):
    if(date1[i]==date2[i]):
        f.write(date1[i] +" "+open1[i]+" "+high1[i]+" "+low1[i]+" "+close1[i]+" "+shares[i]+" "+turnover[i] )
f.close()   
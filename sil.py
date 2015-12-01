__author__ = 'kubrakose'
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import unicodedata
import sqlite3
html=urllib2.urlopen("https://my.sehir.edu.tr/Pages/Duyurular/2015_2016/GuzDersProgrami.aspx").read()
h = html.decode('utf-8')
soup=BeautifulSoup(h)
l=[]
for s in soup.findAll("span"):
    #print(unicodedata.normalize("NFKD",s.getText()).encode('ascii','ignore'))
    l.append(unicodedata.normalize("NFKD",s.getText()).encode('ascii','ignore'))
#print(l)
del l[-3]
del l[-2]
del l[-1]
#print l.index("Course Code")
li=l[29:]
#print li
#for i in li: print i
#print(li.index("CTV 419"))
li.insert(365,"")
def r(x):
    k=[]
    while len(x)>0:
        k.append(tuple(x[0:6]))
        del x[0:6]
    return k
lt=r(li)   #list of tuples
#for r in lt:print(r)

db=sqlite3.connect("program2.db")
im=db.cursor()
im.execute("""CREATE TABLE sehir(ccode, cname, days, time, room, fmember)""")
im.executemany("""INSERT INTO sehir VALUES (?,?,?,?,?,?)""", lt)
db.commit()
data=im.fetchall()
print data
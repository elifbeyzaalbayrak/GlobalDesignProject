__author__ = 'kubrakose'
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import unicodedata
import sqlite3

def ie():
    html=urllib2.urlopen("http://ie.sehir.edu.tr/lisans/").read()
    h = html.decode('utf-8')
    soup=BeautifulSoup(h)
    l=[]
    for s in soup.findAll("td"):
        if (unicodedata.normalize("NFKD",s.getText()).encode("ascii","ignore"))!="&#8211;":
            #print (unicodedata.normalize("NFKD",s.getText()).encode("ascii","ignore"))
            l.append(unicodedata.normalize("NFKD",s.getText()).encode('ascii','ignore'))
    del l[l.index("DEPARTMENTAL ELECTIVESDers KoduDers AdTPLCRECTSOnsart"):]
    l2=["Ders Kodu","Ders Ad","T","P","L","CR","ECTS","Onsart",""]
    #print l
    l3=[]
    for i in l:
        #print(i)
        if "&#8211;" in i: l3.append(i.replace(i[i.index("&"):i.index(";")+1]," "))
            #print i.replace(i[i.index("&"):i.index(";")]," ")
        elif "Ders KoduDers AdTPLCRECTSOnsart" in i: l3.append(i.replace(i[i.index("Ders"):i.index("t")+1]," "))
        elif i not in l2: l3.append(i)
    #print(l3)
    l4=[['I. Donem'],["II. SEMESTER "],["III. Donem "],["IV. Donem "],["V. Donem "],["VI. Donem "],["VII. Donem "],["VIII. Donem "]]
    s=["VIII. Donem ","VII. Donem ","VI. Donem ","V. Donem ","IV. Donem ","III. Donem ","II. SEMESTER ","I. Donem"]
    l5=[]
    for ii in range(len(s)):
        l5.append(l3[l3.index(s[ii]):])
        del l3[l3.index(s[ii]):]
    for i in l5:
        del i[i.index("TOTAL"):i.index("TOTAL")+3]
    for i in l4:
        for f in l5:
            if f[0]==i[0]:
                for c in f[1:]:
                    i.append(c)
    del l4[6][1]
    del l4[3][-1]
    for i in l4:
        if "(non-credit)" in i:
            i.insert(i.index("(non-credit)"),"")
            i.insert(i.index("(non-credit)"),"")
            i.insert(i.index("(non-credit)"),"")
    l4[1].remove("MATH 103")
    l4[3].remove("UNI 123")
    #for i in l4:print i
    #print(l4)
    nl=[]
    dersler=[]
    for x in range(0,len(l4),2):
        nl.append(tuple(l4[x][1:]+l4[x+1][1:]))
    #print(nl)
    for i in range(len(nl)):
        for ii in range(0,len(nl[i]),7):
            if i==0:
                a0=("FRESHMAN YEAR ")
                a1=(nl[i][ii])
                a2=(nl[i][ii+1])
                a3=(nl[i][ii+2])
                a4=(nl[i][ii+3])
                a5=(nl[i][ii+4])
                a6=(nl[i][ii+5])
                a7=(nl[i][ii+6])
                a8=(a0,a1,a2,a3,a4,a5,a6,a7)
                dersler.append(a8)
            if i==1:
                a0=("SOPHOMORE YEAR ")
                a1=(nl[i][ii])
                a2=(nl[i][ii+1])
                a3=(nl[i][ii+2])
                a4=(nl[i][ii+3])
                a5=(nl[i][ii+4])
                a6=(nl[i][ii+5])
                a7=(nl[i][ii+6])
                a8=(a0,a1,a2,a3,a4,a5,a6,a7)
                dersler.append(a8)
            if i==2:
                a0=("JUNIOR YEAR ")
                a1=(nl[i][ii])
                a2=(nl[i][ii+1])
                a3=(nl[i][ii+2])
                a4=(nl[i][ii+3])
                a5=(nl[i][ii+4])
                a6=(nl[i][ii+5])
                a7=(nl[i][ii+6])
                a8=(a0,a1,a2,a3,a4,a5,a6,a7)
                dersler.append(a8)
            if i==3:
                a0=("SENIOR YEAR ")
                a1=(nl[i][ii])
                a2=(nl[i][ii+1])
                a3=(nl[i][ii+2])
                a4=(nl[i][ii+3])
                a5=(nl[i][ii+4])
                a6=(nl[i][ii+5])
                a7=(nl[i][ii+6])
                a8=(a0,a1,a2,a3,a4,a5,a6,a7)
                dersler.append(a8)
    return dersler

ie=ie()


#db=sqlite3.connect("example.db")
#im=db.cursor()
#im.execute("""CREATE TABLE ie(year, ccode, course, T, P, L, CR, EECTS)""")
#im.executemany("""INSERT INTO ie VALUES (?,?,?,?,?,?,?,?)""", ie)
#db.commit()
#data=im.fetchall()
#print data
__author__ = 'kubrakose'
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import unicodedata
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
from lxml.html import parse
import xlrd

def convert(l):
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    li=[]
    for ii in l:
        if ii[-1] not in numbers:
            li.append(ii)
        if ii[-1] in numbers:
            if "non - cre" not in ii[-13:]:
                li.append(ii.replace(ii[-4:],""))
            else:
                 li.append(ii.replace(ii[-13:],""))
    return li

def cs():
    d={}
    d["FRESHMAN YEAR"]=[]
    d["SOPHOMORE YEAR"]=[]
    d["JUNIOR YEAR"]=[]
    d["SENIOR YEAR"]=[]
    html=urllib2.urlopen("http://cs.sehir.edu.tr/programs/und/#crr").read()
    h = html.decode('utf-8')
    soup=BeautifulSoup(h)
    l=[]
    for s in soup.findAll("tr"):
        l.append(unicodedata.normalize("NFKD",s.getText()).encode('ascii','ignore'))
    del l[0:2]
    #print l.index("Computer Science Courses as a Second Major")
    l2=l[120:] #cs as a second and minor
    del l[120:]
    #print l.index("OTHER DEPARTMENTAL or COLLEGE ELECTIVES")
    l3=l[109:] #departmental or college electives
    del l[109:]
    #print l.index("EECS TRACKS and DEPARTMENTAL ELECTIVES - 3 credits each (= 5 ECTS credits)")
    l4=l[77:] #eecs electives
    del l[77:]
    l=[value for value in l if value != "COURSE CODECOURSE NAMETPCRECTS"]
    for i in l:
        if "TOTAL" in i:
            l.remove(i)
    # l-ders programı freshman etc seklinde
    li=convert(l)
    #print(l),len(l)
    #print(li),len(li)
    #for i in li:print i
    d["SENIOR YEAR"]=li[li.index("SENIOR YEAR")+1:]
    del li[li.index("SENIOR YEAR"):]
    d["JUNIOR YEAR"]=li[li.index("JUNIOR YEAR")+1:]
    del li[li.index("JUNIOR YEAR"):]
    d["SOPHOMORE YEAR"]=li[li.index("SOPHOMORE YEAR")+1:]
    del li[li.index("SOPHOMORE YEAR"):]
    d["FRESHMAN YEAR"]=li[li.index("FRESHMAN YEAR")+1:]
    for i in d.keys():
        y=(d[i][d[i].index("II. SEMESTER"):])
        del d[i][d[i].index("II. SEMESTER"):]
        d[i]=((d[i]),y)
    #print(d)
    dersler=[]
    for i in d:
        d[i]=tuple(d[i][0][1:]+d[i][1][1:])
    #print(d)
    ### dönemlik dolayisiyla senelik ders sayilari farkli bu yuzden "" ekledim ###
    dersler.append(d["FRESHMAN YEAR"])
    dersler.append(d["SOPHOMORE YEAR"])
    dersler.append(d["JUNIOR YEAR"])
    dersler.append(d["SENIOR YEAR"])
    dersler[1]=dersler[1]+tuple(" ")+tuple(" ")
    dersler[2]=dersler[2]+tuple(" ")
    dersler[3]=dersler[3]+tuple(" ")+tuple(" ")+tuple(" ")+tuple(" ")
    #for items in dersler: print len(items),items
    return dersler

'''
********** ee bolum sayfasındaki ders programı eskii  *************
:return:
'''
def ee():
    l=[]
    e=["FRESHMAN YEAR","SOPHOMORE YEAR","JUNIOR YEAR","SENIOR YEAR","COURSE CODE","COURSE NAME","T","P","L","CR","ECTS","PRE-REQ.","PRE- REQ.","NONE","TOTAL","(non-credit)"]
    s=[["VIII. SEMESTER",""],["VII. SEMESTER",""],["VI. SEMESTER",""],["V. SEMESTER",""],["IV. SEMESTER",""],["III. SEMESTER",""],["II. SEMESTER",""],['I. SEMESTER', '']]
    p=xlrd.open_workbook("Workbook1.xlsx")
    sh = p.sheet_by_index(0)
    for i in range(sh.nrows):
        l.append(sh.row_values(i))
    l2=[]
    for ii in l:
        if ii[0]!="":
            if ii[0] not in e:
                l2.append(ii[0:2])
    #for i in l2: print(i)
    l3=[]
    l4=[['I. SEMESTER'],["II. SEMESTER"],["III. SEMESTER"],["IV. SEMESTER"],["V. SEMESTER"],["VI. SEMESTER"],["VII. SEMESTER"],["VIII. SEMESTER"]]
    for ii in range(len(s)):
        l3.append(l2[l2.index(s[ii]):])
        del l2[l2.index(s[ii]):]
    for i in l4:
        for f in l3:
            if f[0][0]==i[0]:
                for c in f[1:]:
                    for cc in c:
                        i.append((unicodedata.normalize("NFKD",cc).encode('ascii','ignore')))
    #print(l4)
    nl=[]
    dersler=[]
    for x in range(0,len(l4),2):
        nl.append(tuple(l4[x][1:]+l4[x+1][1:]))
    #print(nl)
    for i in range(len(nl)):
        dersler.append(len(nl[i])*[])
        for ii in range(0,len(nl[i]),2):
            dersler[i].append((nl[i][ii]+" "+nl[i][ii+1]))
    print(dersler)
    dersler[1]=dersler[1]+[" "," "]
    dersler[2]=dersler[2]+[" "," "]
    dersler[3]=dersler[3]+[" "," "," "," "," "]
    #for f in dersler: print len(f),f
    return dersler

def ie():
    html=urllib2.urlopen("http://ie.sehir.edu.tr/lisans/").read()
    h = html.decode('utf-8')
    soup=BeautifulSoup(h)
    l=[]
    for s in soup.findAll("strong"):
        l.append(unicodedata.normalize("NFKD",s.getText()).encode('ascii','ignore'))
    l2=l[l.index("ELECTIVE COURSES"):] # l2 is the list for elective courses
    del l[l.index("ELECTIVE COURSES"):]
    del l[:(l.index("CORE COURSES"))+1]
    for i in l:print i

cs=cs()
ee=ee()




'''
ie deneme
    html=urllib2.urlopen("http://ie.sehir.edu.tr/lisans/").read()
    h = html.decode('utf-8')
    soup=BeautifulSoup(h)
    l=[]
    for s in soup.findAll("table"):
        print s.getText()
    #t=soup.find("table")
    #datasets = []
    #for row in t.find_all("tr")[1:]:
    #    print(row)
    #print datasets
'''
db=sqlite3.connect("programcs.db")
im=db.cursor()
im.execute("""CREATE TABLE ee(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)""")
im.executemany("""INSERT INTO ee VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", ee)
db.commit()
data=im.fetchall()
print data
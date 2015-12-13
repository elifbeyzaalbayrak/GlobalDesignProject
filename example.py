__author__ = 'kubrakose'
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import unicodedata
import sqlite3
import xlrd


def cs():
    l=[]
    p=xlrd.open_workbook("Workbookcs.xlsx")
    sh = p.sheet_by_index(0)
    for i in range(sh.nrows):
        l.append(sh.row_values(i))
    #print(l)
    l2=[]
    q=["",'COURSE CODE', 'COURSE NAME', 'T', 'P', 'L', 'CR', 'ECTS', 'PRE-REQ.',"PRE- REQ.",'I. SEMESTER',"II. SEMESTER","III. SEMESTER",'IV. SEMESTER','V. SEMESTER','VI. SEMESTER','VII. SEMESTER','VIII. SEMESTER']
    for i in l:
        for ii in i:
            if type(ii)==unicode:
                if (unicodedata.normalize("NFKD",ii).encode('ascii','ignore')) not in q:
                    l2.append(unicodedata.normalize("NFKD",ii).encode('ascii','ignore'))
            elif ii not in q: l2.append(ii)
    c=[]
    ctype=["CORE COURSES ELECTIVES","EECS TRACKS and DEPARTMENTAL ELECTIVES"]
    c.append(l2[:l2.index(ctype[1])]) #zorunlular
    c.append(l2[l2.index(ctype[1])+1:l2.index(ctype[0])]) #deparmentals
    c.append(l2[l2.index(ctype[0])+1:]) #ortak dersler
    c[1].remove('COMPUTER SYSTEMS')
    c[1].remove('THEORY and ALGORITHMS')
    c[1].remove('EE SYSTEMS')
    c[1].remove("DEVICES")
    c[1].remove('OTHER DEPARTMENTAL or COLLEGE ELECTIVES')
    #for r in c:print r
    c2=[]
    c2.append(c[0][1:c[0].index("SOPHOMORE YEAR")])
    c2.append(c[0][c[0].index("SOPHOMORE YEAR")+1:c[0].index("JUNIOR YEAR")])
    c2.append(c[0][c[0].index("JUNIOR YEAR")+1:c[0].index("SENIOR YEAR")])
    c2.append(c[0][c[0].index("SENIOR YEAR")+1:])
    #print (c2)
    #for i in c2:
    #    for ii in i:print type(ii), ii
    dersler=[]
    #for i in (c2[1]):print i
    for i in range(len(c2)):
        for ii in range(0,len(c2[i]),8):
            if i==0:
                a0=("FRESHMAN YEAR")
                a1=(c2[i][ii]);a2=(c2[i][ii+1]);a3=(c2[i][ii+2])
                a4=(c2[i][ii+3]);a5=(c2[i][ii+4]);a6=(c2[i][ii+5])
                a7=(c2[i][ii+6]);a8=(c2[i][ii+7])
                a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
                dersler.append(a9)
            if i==1:
                a0=("SOPHOMORE YEAR")
                a1=(c2[i][ii]);a2=(c2[i][ii+1]);a3=(c2[i][ii+2])
                a4=(c2[i][ii+3]);a5=(c2[i][ii+4]);a6=(c2[i][ii+5])
                a7=(c2[i][ii+6]);a8=(c2[i][ii+7])
                a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
                dersler.append(a9)
            if i==2:
                a0=("JUNIOR YEAR")
                a1=(c2[i][ii])
                a2=(c2[i][ii+1])
                a3=(c2[i][ii+2])
                a4=(c2[i][ii+3])
                a5=(c2[i][ii+4])
                a6=(c2[i][ii+5])
                a7=(c2[i][ii+6])
                a8=(c2[i][ii+7])
                a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
                dersler.append(a9)
            if i==3:
                a0=("SENIOR YEAR")
                a1=(c2[i][ii])
                a2=(c2[i][ii+1])
                a3=(c2[i][ii+2])
                a4=(c2[i][ii+3])
                a5=(c2[i][ii+4])
                a6=(c2[i][ii+5])
                a7=(c2[i][ii+6])
                a8=(c2[i][ii+7])
                a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
                dersler.append(a9)
    #for i in c[1]:print i
    for i in range(0,len(c[1]),8):
        a0=("Departmental Electives");a1=(c[1][i]);a2=(c[1][i+1])
        a3=(c[1][i+2]);a4=(c[1][i+3]);a5=(c[1][i+4])
        a6=(c[1][i+5]);a7=(c[1][i+6]);a8=(c[1][i+7])
        a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
        dersler.append(a9)
    for i in range(0,len(c[1]),8):
        a0=("Core Courses");a1=(c[1][i]);a2=(c[1][i+1])
        a3=(c[1][i+2]);a4=(c[1][i+3]);a5=(c[1][i+4])
        a6=(c[1][i+5]);a7=(c[1][i+6]);a8=(c[1][i+7])
        a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
        dersler.append(a9)
    #for i in dersler: print i
    return dersler
cs=cs()


def ie():
    l=[]
    p=xlrd.open_workbook("Workbookie.xlsx")
    sh = p.sheet_by_index(0)
    for i in range(sh.nrows):
        l.append(sh.row_values(i))
    #print(l)
    l2=[]
    q=["",'COURSE CODE', 'COURSE NAME', 'T', 'P', 'L', 'CR', 'ECTS', 'PRE-REQ.',"PRE- REQ.",'I. SEMESTER',"II. SEMESTER","III. SEMESTER",'IV. SEMESTER','V. SEMESTER','VI. SEMESTER','VII. SEMESTER','VIII. SEMESTER']
    for i in l:
        for ii in i:
            if type(ii)==unicode:
                if (unicodedata.normalize("NFKD",ii).encode('ascii','ignore')) not in q:
                    l2.append(unicodedata.normalize("NFKD",ii).encode('ascii','ignore'))
            elif ii not in q: l2.append(ii)
    c=[]
    ctype=["CORE COURSES ELECTIVES","DEPARTMENTAL ELECTIVES"]
    c.append(l2[:l2.index(ctype[1])]) #zorunlular
    c.append(l2[l2.index(ctype[1])+1:l2.index(ctype[0])]) #deparmentals
    c.append(l2[l2.index(ctype[0])+1:]) #ortak dersler
    c[1].remove("DEPARTMENTAL ELECTIVES FROM SCHOOL OF MANAGEMENT AND ADMINISTRATIVE SCIENCES")
    #for r in c:print r
    c2=[]
    c2.append(c[0][1:c[0].index("SOPHOMORE YEAR")])
    c2.append(c[0][c[0].index("SOPHOMORE YEAR")+1:c[0].index("JUNIOR YEAR")])
    c2.append(c[0][c[0].index("JUNIOR YEAR")+1:c[0].index("SENIOR YEAR")])
    c2.append(c[0][c[0].index("SENIOR YEAR")+1:])
    #print (c2)
    #for i in c2:
    #    for ii in i:print type(ii), ii
    dersler=[]
    #for i in (c2[1]):print i
    for i in range(len(c2)):
        for ii in range(0,len(c2[i]),8):
            if i==0:
                a0=("FRESHMAN YEAR")
                a1=(c2[i][ii]);a2=(c2[i][ii+1]);a3=(c2[i][ii+2])
                a4=(c2[i][ii+3]);a5=(c2[i][ii+4]);a6=(c2[i][ii+5])
                a7=(c2[i][ii+6]);a8=(c2[i][ii+7])
                a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
                dersler.append(a9)
            if i==1:
                a0=("SOPHOMORE YEAR")
                a1=(c2[i][ii]);a2=(c2[i][ii+1]);a3=(c2[i][ii+2])
                a4=(c2[i][ii+3]);a5=(c2[i][ii+4]);a6=(c2[i][ii+5])
                a7=(c2[i][ii+6]);a8=(c2[i][ii+7])
                a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
                dersler.append(a9)
            if i==2:
                a0=("JUNIOR YEAR")
                a1=(c2[i][ii])
                a2=(c2[i][ii+1])
                a3=(c2[i][ii+2])
                a4=(c2[i][ii+3])
                a5=(c2[i][ii+4])
                a6=(c2[i][ii+5])
                a7=(c2[i][ii+6])
                a8=(c2[i][ii+7])
                a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
                dersler.append(a9)
            if i==3:
                a0=("SENIOR YEAR")
                a1=(c2[i][ii])
                a2=(c2[i][ii+1])
                a3=(c2[i][ii+2])
                a4=(c2[i][ii+3])
                a5=(c2[i][ii+4])
                a6=(c2[i][ii+5])
                a7=(c2[i][ii+6])
                a8=(c2[i][ii+7])
                a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
                dersler.append(a9)
    #for i in c[1]:print i
    for i in range(0,len(c[1]),8):
        a0=("Departmental Electives");a1=(c[1][i]);a2=(c[1][i+1])
        a3=(c[1][i+2]);a4=(c[1][i+3]);a5=(c[1][i+4])
        a6=(c[1][i+5]);a7=(c[1][i+6]);a8=(c[1][i+7])
        a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
        dersler.append(a9)
    for i in range(0,len(c[2]),8):
        a0=("Core Courses");a1=(c[2][i]);a2=(c[2][i+1])
        a3=(c[1][i+2]);a4=(c[2][i+3]);a5=(c[1][i+4])
        a6=(c[1][i+5]);a7=(c[2][i+6]);a8=(c[2][i+7])
        a9=(a0,a1,a2,a3,a4,a5,a6,a7,a8)
        dersler.append(a9)
    #for i in dersler: print i
    return dersler
ie=ie()
#db=sqlite3.connect("example.db")
#im=db.cursor()
##im.execute("""DROP TABLE ie""")
#im.execute("""CREATE TABLE ie(year, ccode, course, T, P, L, CR, EECTS, pr)""")
#im.executemany("""INSERT INTO ie VALUES (?,?,?,?,?,?,?,?,?)""", ie)
#db.commit()
#data=im.fetchall()

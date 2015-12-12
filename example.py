__author__ = 'kubrakose'
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import unicodedata
import sqlite3
import xlrd


def ie():
    html = urllib2.urlopen("http://ie.sehir.edu.tr/lisans/").read()
    h = html.decode('utf-8')
    soup = BeautifulSoup(h)
    l = []
    for s in soup.findAll("td"):
        if (unicodedata.normalize("NFKD", s.getText()).encode("ascii", "ignore")) != "&#8211;":
            # print (unicodedata.normalize("NFKD",s.getText()).encode("ascii","ignore"))
            l.append(unicodedata.normalize("NFKD", s.getText()).encode('ascii', 'ignore'))
    del l[l.index("DEPARTMENTAL ELECTIVESDers KoduDers AdTPLCRECTSOnsart"):]
    l2 = ["Ders Kodu", "Ders Ad", "T", "P", "L", "CR", "ECTS", "Onsart", ""]
    # print l
    l3 = []
    for i in l:
        # print(i)
        if "&#8211;" in i:
            l3.append(i.replace(i[i.index("&"):i.index(";") + 1], " "))
        # print i.replace(i[i.index("&"):i.index(";")]," ")
        elif "Ders KoduDers AdTPLCRECTSOnsart" in i:
            l3.append(i.replace(i[i.index("Ders"):i.index("t") + 1], " "))
        elif i not in l2:
            l3.append(i)
    # print(l3)
    l4 = [['I. Donem'], ["II. SEMESTER "], ["III. Donem "], ["IV. Donem "], ["V. Donem "], ["VI. Donem "],
          ["VII. Donem "], ["VIII. Donem "]]
    s = ["VIII. Donem ", "VII. Donem ", "VI. Donem ", "V. Donem ", "IV. Donem ", "III. Donem ", "II. SEMESTER ",
         "I. Donem"]
    l5 = []
    for ii in range(len(s)):
        l5.append(l3[l3.index(s[ii]):])
        del l3[l3.index(s[ii]):]
    for i in l5:
        del i[i.index("TOTAL"):i.index("TOTAL") + 3]
    for i in l4:
        for f in l5:
            if f[0] == i[0]:
                for c in f[1:]:
                    i.append(c)
    del l4[6][1]
    del l4[3][-1]
    for i in l4:
        if "(non-credit)" in i:
            i.insert(i.index("(non-credit)"), "")
            i.insert(i.index("(non-credit)"), "")
            i.insert(i.index("(non-credit)"), "")
    l4[1].remove("MATH 103")
    l4[3].remove("UNI 123")
    # for i in l4:print i
    # print(l4)
    nl = []
    dersler = []
    for x in range(0, len(l4), 2):
        nl.append(tuple(l4[x][1:] + l4[x + 1][1:]))
    # print(nl)
    for i in range(len(nl)):
        for ii in range(0, len(nl[i]), 7):
            if i == 0:
                a0 = ("FRESHMAN YEAR ")
                a1 = (nl[i][ii])
                a2 = (nl[i][ii + 1])
                a3 = (nl[i][ii + 2])
                a4 = (nl[i][ii + 3])
                a5 = (nl[i][ii + 4])
                a6 = (nl[i][ii + 5])
                a7 = (nl[i][ii + 6])
                a8 = (a0, a1, a2, a3, a4, a5, a6, a7)
                dersler.append(a8)
            if i == 1:
                a0 = ("SOPHOMORE YEAR ")
                a1 = (nl[i][ii])
                a2 = (nl[i][ii + 1])
                a3 = (nl[i][ii + 2])
                a4 = (nl[i][ii + 3])
                a5 = (nl[i][ii + 4])
                a6 = (nl[i][ii + 5])
                a7 = (nl[i][ii + 6])
                a8 = (a0, a1, a2, a3, a4, a5, a6, a7)
                dersler.append(a8)
            if i == 2:
                a0 = ("JUNIOR YEAR ")
                a1 = (nl[i][ii])
                a2 = (nl[i][ii + 1])
                a3 = (nl[i][ii + 2])
                a4 = (nl[i][ii + 3])
                a5 = (nl[i][ii + 4])
                a6 = (nl[i][ii + 5])
                a7 = (nl[i][ii + 6])
                a8 = (a0, a1, a2, a3, a4, a5, a6, a7)
                dersler.append(a8)
            if i == 3:
                a0 = ("SENIOR YEAR ")
                a1 = (nl[i][ii])
                a2 = (nl[i][ii + 1])
                a3 = (nl[i][ii + 2])
                a4 = (nl[i][ii + 3])
                a5 = (nl[i][ii + 4])
                a6 = (nl[i][ii + 5])
                a7 = (nl[i][ii + 6])
                a8 = (a0, a1, a2, a3, a4, a5, a6, a7)
                dersler.append(a8)
    return dersler


ie = ie()


def ie_electives():
    html = urllib2.urlopen("http://ie.sehir.edu.tr/lisans/").read()
    h = html.decode('utf-8')
    soup = BeautifulSoup(h)
    l = []
    for s in soup.findAll("td"):
        if (unicodedata.normalize("NFKD", s.getText()).encode("ascii", "ignore")) != "&#8211;":
            # print (unicodedata.normalize("NFKD",s.getText()).encode("ascii","ignore"))
            l.append(unicodedata.normalize("NFKD", s.getText()).encode('ascii', 'ignore'))
    del l[:l.index("DEPARTMENTAL ELECTIVESDers KoduDers AdTPLCRECTSOnsart")]
    del l[l.index("GROUP A"):]
    # for i in l:print i
    l2 = ["Ders Kodu", "Ders Ad", "T", "P", "L", "CR", "ECTS", "Onsart", ""]
    l3 = []
    for i in l:
        # print(i)
        if "&#8211;" in i:
            l3.append(i.replace(i[i.index("&"):i.index(";") + 1], " "))
        # print i.replace(i[i.index("&"):i.index(";")]," ")
        elif "Ders KoduDers AdTPLCRECTSOnsart" in i:
            l3.append(i.replace(i[i.index("Ders"):i.index("t") + 1], " "))
        elif i not in l2:
            l3.append(i)
    # for i in l3:print(i)
    new = []
    li = ["DEPARTMENTAL ELECTIVES FROM SCHOOL OF MANAGEMENT AND ADMINISTRATIVE SCIENCES ", ".",
          "DEPARTMENTAL ELECTIVES ", "THE POOL OF COURSES CURRICULUM "]
    new.append(list(l3[:l3.index("DEPARTMENTAL ELECTIVES FROM SCHOOL OF MANAGEMENT AND ADMINISTRATIVE SCIENCES ")]))
    new.append(list(l3[
                    l3.index("DEPARTMENTAL ELECTIVES FROM SCHOOL OF MANAGEMENT AND ADMINISTRATIVE SCIENCES "):l3.index(
                        "THE POOL OF COURSES CURRICULUM ")]))
    new.append(list(l3[l3.index("THE POOL OF COURSES CURRICULUM ") + 2:]))
    for i in new:
        for ii in i:
            if ii in li:
                i.remove(ii)
    w = []
    for r in new[1]:
        if r == "5":
            w.append(new[1][:new[1].index(r) + 1])
            del (new[1][:new[1].index(r) + 1])
    del new[1][-1]
    new[1] = [value for value in new[1] if value != "MGT 203"]
    p = 0
    while p < 6:
        for z in new[1]:
            if z == "5":
                w.append(new[1][:new[1].index(z) + 1])
                del (new[1][:new[1].index(z) + 1])
                p = p + 1
    for i in w:
        if i[0] == "MGT 204":
            i.append("MGT 203")
        if i[0] == "MGT 303":
            i.append("MGT 203")
        if i[0] == "MGT 442":
            i.append("MGT 204")
        else:
            i.append("NONE")
    del w[5][-1]
    del w[7][-1]
    del new[1]
    dersler = []
    # for i in new: print i
    for i in range(len(new)):
        for ii in range(0, len(new[i]), 8):
            if i == 0:
                a0 = ("Departmental Electives")
                a1 = (new[i][ii])
                a2 = (new[i][ii + 1])
                a3 = (new[i][ii + 2])
                a4 = (new[i][ii + 3])
                a5 = (new[i][ii + 4])
                a6 = (new[i][ii + 5])
                a7 = (new[i][ii + 6])
                a8 = (new[i][ii + 7])
                a9 = (a0, a1, a2, a3, a4, a5, a6, a7, a8)
                dersler.append(a9)
            if i == 1:
                a0 = ("Core Courses")
                a1 = (new[i][ii])
                a2 = (new[i][ii + 1])
                a3 = (new[i][ii + 2])
                a4 = (new[i][ii + 3])
                a5 = (new[i][ii + 4])
                a6 = (new[i][ii + 5])
                a7 = (new[i][ii + 6])
                a8 = (new[i][ii + 7])
                a9 = (a0, a1, a2, a3, a4, a5, a6, a7, a8)
                dersler.append(a9)
    for i in (w):
        i.insert(0, "Departmental Electives")
    for i in w:
        dersler.append(tuple(i))
    # for i in dersler: print(i)
    return dersler


ie2 = ie_electives()

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

#db=sqlite3.connect("example.db")
#im=db.cursor()
##im.execute("""DROP TABLE cs""")
#im.execute("""CREATE TABLE cs(year, ccode, course, T, P, L, CR, EECTS, PRQ)""")
#im.executemany("""INSERT INTO cs VALUES (?,?,?,?,?,?,?,?,?)""", cs)
#db.commit()
#data=im.fetchall()
#print data
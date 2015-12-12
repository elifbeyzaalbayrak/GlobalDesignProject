__author__ = 'kubrakose'
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import unicodedata
import sqlite3


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

# db=sqlite3.connect("example.db")
# im=db.cursor()
# im.execute("""CREATE TABLE ie2(year, ccode, course, T, P, L, CR, EECTS, pr)""")
# im.executemany("""INSERT INTO ie2 VALUES (?,?,?,?,?,?,?,?,?)""", ie2)
# db.commit()
# data=im.fetchall()
# print data


# db=sqlite3.connect("example.db")
# im=db.cursor()
# im.execute("""CREATE TABLE ie(year, ccode, course, T, P, L, CR, EECTS)""")
# im.executemany("""INSERT INTO ie VALUES (?,?,?,?,?,?,?,?)""", ie)
# db.commit()
# data=im.fetchall()
# print data

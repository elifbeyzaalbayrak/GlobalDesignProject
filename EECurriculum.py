import csv
import sqlite3

with open("EECurriculum.csv","rb") as f:
    for i in range(3):
        f.readline()
    reader=csv.reader(f)
    lst=list(reader)
    fresman_year=[]
    fresman_year2=[]
    sophomore_year=[]
    sophomore_year2=[]
    junior_year=[]
    junior_year2=[]
    senior_year=[]
    senior_year2=[]
    core_course_elective=[]
    core_course_elective2=[]
    departmental_elective=[]
    departmental_elective2=[]
    counter=0
    counter2=20
    counter3=42
    counter4=64
    counter5=132
    counter6=84

    while lst[counter][0]!="SOPHOMORE YEAR":
            fresman_year.append(lst[counter])
            counter+=1
    for i in fresman_year:
        if i[1]!='':
                 if i[1]!='COURSE NAME':
                     fresman_year2.append(tuple(i))

    while lst[counter2][0]!="JUNIOR YEAR":
            sophomore_year.append(lst[counter2])
            counter2+=1
    for a in sophomore_year:
        if a[1]!='':
                 if a[1]!='COURSE NAME':
                     sophomore_year2.append(tuple(a))

    while lst[counter3][0]!="SENIOR YEAR":
            junior_year.append(lst[counter3])
            counter3+=1
    for b in junior_year:
        if b[1]!='':
                 if b[1]!='COURSE NAME':
                     junior_year2.append(tuple(b))

    while lst[counter4][0]!="COMPUTER SYSTEMS":
            senior_year.append(lst[counter4])
            counter4+=1
    for c in senior_year:
        if c[1]!='':
                 if c[1]!='COURSE NAME':
                     senior_year2.append(tuple(c))

    while lst[counter5][0]!='NOTES:':
            core_course_elective.append(lst[counter5])
            counter5+=1
    for d in core_course_elective:
        if d[1]!='':
                 if d[1]!='COURSE NAME':
                     core_course_elective2.append(tuple(d))

    while lst[counter6][0]!='?':
            departmental_elective.append(lst[counter6])
            counter6+=1
    for e in departmental_elective:
        if e[1]!='':
                 if e[1]!='COURSE NAME':
                     departmental_elective2.append(tuple(e))



####################################DATABASE###########################################################
db=sqlite3.connect("ee_curriculum.db")
im=db.cursor()
#im.execute("""CREATE TABLE ee_curriculum(course_code,course_name,t,p,l,cr,ects,pre_req,year)""")
#for cc,cn,t,p,l,cr,ects,pre_req in fresman_year2:
 #  im.execute("""INSERT INTO ee_curriculum VALUES (?,?,?,?,?,?,?,?,?)""",(cc,cn,t,p,l,cr,ects,pre_req,'freshman'))
#db.commit()
#for cc,cn,t,p,l,cr,ects,pre_req in sophomore_year2:
 #  im.execute("""INSERT INTO ee_curriculum VALUES (?,?,?,?,?,?,?,?,?)""",(cc,cn,t,p,l,cr,ects,pre_req,'sophomore'))
#db.commit()
#for cc,cn,t,p,l,cr,ects,pre_req in junior_year2:
#   im.execute("""INSERT INTO ee_curriculum VALUES (?,?,?,?,?,?,?,?,?)""",(cc,cn,t,p,l,cr,ects,pre_req,'junior'))
#db.commit()
#for cc,cn,t,p,l,cr,ects,pre_req in senior_year2:
 # im.execute("""INSERT INTO ee_curriculum VALUES (?,?,?,?,?,?,?,?,?)""",(cc,cn,t,p,l,cr,ects,pre_req,'senior'))
#db.commit()
#for cc,cn,t,p,l,cr,ects,pre_req in departmental_elective2:
 #  im.execute("""INSERT INTO ee_curriculum VALUES (?,?,?,?,?,?,?,?,?)""",(cc,cn,t,p,l,cr,ects,pre_req,'departmental'))
#db.commit()
#for cc,cn,t,p,l,cr,ects,pre_req in core_course_elective2:
 # im.execute("""INSERT INTO ee_curriculum VALUES (?,?,?,?,?,?,?,?,?)""",(cc,cn,t,p,l,cr,ects,pre_req,'core_course'))
#db.commit()
im.execute("""SELECT * FROM ee_curriculum """)
data=im.fetchall()
for v in data:
    print(v)










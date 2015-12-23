from django.db import models

# Create your models here.
from django import forms
import sqlite3
from django.core.files import File


def derslerbolum():
    d=[]
    conn=sqlite3.connect("deneme.db")
    cs=conn.cursor()
    cs.execute("""SELECT * FROM cs""")
    verics=cs.fetchall()
    for items in verics:
        if items[0:4] not in d:
            d.append(items[0:4])
    ee=conn.cursor()
    ee.execute(""" SELECT * FROM ee """)
    veriee=ee.fetchall()
    for itemse in veriee:
        if itemse[0:4] not in d:
            d.append(itemse[0:4])
    ie=conn.cursor()
    ie.execute(""" SELECT * FROM ie """)
    veriie=ie.fetchall()
    for items1 in veriie:
        if items1[0:4] not in d:
            d.append(items1[0:4])
    return d

d=[]
def dersler():
    conn=sqlite3.connect("deneme.db")
    cs=conn.cursor()
    cs.execute("""SELECT * FROM cs""")
    verics=cs.fetchall()
    for items in verics:
        if items[2:4] not in d:
            d.append(items[2:4])
    ee=conn.cursor()
    ee.execute(""" SELECT * FROM ee """)
    veriee=ee.fetchall()
    for itemse in veriee:
        if itemse[2:4] not in d:
            d.append(itemse[2:4])
    ie=conn.cursor()
    ie.execute(""" SELECT * FROM ie """)
    veriie=ie.fetchall()
    for items1 in veriie:
        if items1[2:4] not in d:
            d.append(items1[2:4])
    return d

class CountryForm(forms.Form):
        OPTIONS = d
        Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)

#bolumleri secmek icin
def db():
    empty=[]
    conn=sqlite3.connect("deneme.db")
    cs=conn.cursor()
    cs.execute("""SELECT * FROM cs""")
    verics=cs.fetchall()
    for items in verics:
        if items[0] not in empty:
            empty.append(items[0])
    ee=conn.cursor()
    ee.execute(""" SELECT * FROM ee """)
    veriee=ee.fetchall()
    for itemse in veriee:
        if itemse[0] not in empty:
            empty.append(itemse[0])
    ie=conn.cursor()
    ie.execute(""" SELECT * FROM ie """)
    veriie=ie.fetchall()
    for items1 in veriie:
        if items1[0] not in empty:
            empty.append(items1[0])
    return empty



class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    createddate=models.DateTimeField()

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
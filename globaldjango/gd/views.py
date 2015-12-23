from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt,csrf_protect
import unicodedata
from django.shortcuts import render_to_response
import sqlite3
from models import Category
from models import db,dersler,derslerbolum
from django.template import RequestContext
from models import CountryForm
from django.views.generic import View

@csrf_protect
@csrf_exempt
def mys(request):
    if request.method == "POST":
        r0=request.POST.getlist("items[]")
        #print(r0[0][3:5])
        a=(unicodedata.normalize("NFKD",(r0[0][3:5])).encode('ascii','ignore')).lower()
        #print(a)
        conn=sqlite3.connect("deneme.db")
        s=conn.cursor()
        s.execute("SELECT sehir.ccode,sehir.cname,sehir.days,sehir.time,sehir.room,sehir.fmember FROM sehir INNER JOIN (%s) ON sehir.cname=course" %(a))
        sehir=s.fetchall()
        return render_to_response("h3.html",{"ii":sehir})


@csrf_exempt
def mysearch(request):
    l=[]
    if request.method == "GET":
        data=db()
        c=dersler()
        return render_to_response("base.html",{"bolumler":data})

    elif request.method == "POST":
        v=derslerbolum()
        searchbolum = request.POST.get("bolum")
        for i in v:
            if searchbolum==i[0]:
                #l.append(i[2:4])
                l.append(i[0:4])
        return render_to_response("yeni.html",{"bb":l}, context_instance=RequestContext(request))


categories = Category.objects.filter()
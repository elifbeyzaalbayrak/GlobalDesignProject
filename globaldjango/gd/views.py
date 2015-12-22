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

        data=[]

        conn=sqlite3.connect("program2.db")
        s=conn.cursor()
        s.execute("""SELECT * FROM sehir""")
        sehir=s.fetchall()
        for items in sehir:
            for items2 in r0:
                if items2[0] not in items[0] and items2[1] not in items[1]:
                    if items not in data:
                        data.append(items)
        return render_to_response("h3.html",{"ii":data})


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
                l.append(i[2:4])
        return render_to_response("yeni.html",{"bb":l}, context_instance=RequestContext(request))




categories = Category.objects.filter()
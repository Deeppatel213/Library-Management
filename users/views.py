from django.shortcuts import render,HttpResponse
from .models import Booksdata

# Create your views here.
def home(req):
    count=0
    x = Booksdata.objects.all()
    b = []
    for i in x:
        if count==100:
              break
        b.append(i)
        count+=1
    next_id = i.id
    return render(req,'home.html',{'x':b,'next_id':next_id})
def join_hood(req,id):
    a = []
    for i in range(100):
        temp = Booksdata.objects.get(id=id+i)
        a.append(temp)
    next_id = id+100
    if id<100:
        prev_id = 1
    else:
        prev_id = id-100
    return render(req,'home.html',{'x':a,'next_id':next_id,'prev_id': prev_id})
from django.shortcuts import render,redirect
from users.models import Booksdata
# Create your views here.

def adminpanel(req):
    return render(req,'adminpanel.html')

def register(req):
    x = Booksdata.objects.all()
    if req.method=='POST':
        global confirm_id
        bookid = req.POST['bookid']
        confirm_id = bookid
        print(bookid)
        bookid = int(bookid)
        studentid = req.POST['studentid']
        book = Booksdata.objects.filter(id = bookid)
        return render(req,'confirm.html',{'books':book})
    return render(req,'register.html',{'x':x})

def confirm(req):
    book = Booksdata.objects.filter(id = confirm_id)
    print(book)
    return redirect('/adminpanel/register')
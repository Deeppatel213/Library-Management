from django.shortcuts import render,redirect
from users.models import Booksdata
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  database="student_data"
)
# Create your views here.

def adminpanel(req):
    return render(req,'adminpanel.html')

def register(req):
    x = Booksdata.objects.all()
    if req.method=='POST':
        global confirm_id
        global studentid
        bookid = req.POST['bookid']
        confirm_id = bookid
        bookid = int(bookid)
        studentid = req.POST['studentid']
        book = Booksdata.objects.filter(id = bookid)
        cursor = conn.cursor()
        sql = "Select * from new_data where Student_id = " + str(studentid)
        cursor.execute(sql)
        result = cursor.fetchone();
        if result == None:
            invalid_userid = True
            return render(req,'confirm.html',{'invalid_userid':invalid_userid})
        invalid_userid = False
        result = list(result)
        invalid_bookid = True
        for i in book:
            invalid_bookid = False
        return render(req,'confirm.html',{'books':book,'stud_name':result[1],'gender':result[2],'depart':result[3],'stud_id':result[0],"invalid_userid":invalid_userid,'invalid_bookid':invalid_bookid})
    return render(req,'register.html',{'x':x})

def confirm(req):
    book = Booksdata.objects.filter(id = confirm_id)
    print(book)
    cursor = conn.cursor()
    sql = "Select * from new_data where Student_id = " + str(studentid)
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchone();
    result = list(result)
    print(result[1])
    return redirect('/adminpanel/register')
from django.shortcuts import render,HttpResponse,redirect
from .models import Booksdata
from django.db.models import Q
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    if User is not None:
        pass
    if request.method == 'POST':
        title = request.POST['search']
        if (len(title)<3):
            count=0
            x = Booksdata.objects.all()
            b = []
            for i in x:
                if count==100:
                    break
                b.append(i)
                count+=1
            next_id = i.id
            default_view = True
            no_result_found = False
            return render(request,'home.html',{'x':b,'next_id':next_id,'d_v':default_view,'no_result_found':no_result_found})    
        print(title)
        default_view = False
        x = Booksdata.objects.filter(Q(title__icontains=title) | Q(authors__icontains=title) | Q(publisher__icontains=title))
        if len(x)==0:
            no_result_found=True
        else:
            no_result_found = False
        return render(request,'home.html',{'x':x,'d_v':default_view,'prev_id': 1,'no_result_found':no_result_found})
    else:
        count=0
        x = Booksdata.objects.all()
        b = []
        for i in x:
            if count==100:
                break
            b.append(i)
            count+=1
        next_id = i.id
        default_view = True
        no_result_found = False
        return render(request,'home.html',{'x':b,'next_id':next_id,'d_v':default_view,'prev_id': 1,'no_result_found':no_result_found})
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
    default_view = True
    no_result_found = False
    return render(req,'home.html',{'x':a,'next_id':next_id,'prev_id': prev_id,'d_v':default_view,'no_result_found':no_result_found})


def login(request):
    global user
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        username = request.user.username
        if user is not None:
            auth.login(request, user)
            print('loged in')
            return redirect('/adminpanel/')
        else:
            print('user not found')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
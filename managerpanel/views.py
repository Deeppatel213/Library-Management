from django.shortcuts import render

# Create your views here.

def adminpanel(req):
    print('Hiii')
    print("Hello")
    return render(req,'adminpanel.html')
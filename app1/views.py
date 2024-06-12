# Create your views here.
from django.shortcuts import render
def home(request):
    factorial=1
    n1=5
    for i in range(1,n1+1,1):
        factorial=factorial*i
        
    square=n1*n1
    return render(request,'index.html',{'param1':factorial,'param2':n1,'param3':square})

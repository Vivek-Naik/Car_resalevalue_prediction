from django.shortcuts import render

# Create your views here.
def home(request):
    result=getFact(8)
    return render(request,'app3/index.html',{'param1':result})

def getFact(limit):
    factorial=[]
    numbers=[]
    for j in range(3,limit+1,1):
        n1=j
        fact1=1
        for i in range(1,n1+1,1):
            fact1=fact1*i
        factorial.append(fact1)
        numbers.append(n1)
    return zip(factorial,numbers)
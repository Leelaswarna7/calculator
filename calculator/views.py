from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    result= 'None'
    if request.method=='POST':
        a= int(request.POST.get('Num1'))
        b= int(request.POST.get('Num2'))
        op=request.POST.get('op')
        if op=='add':
            result=a+b
        return render(request,'home.html',{'result':result})
    return render(request,'home.html')
def hello(request):
    return HttpResponse("Leela")
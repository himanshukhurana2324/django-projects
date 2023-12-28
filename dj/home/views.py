from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def message(request):
    return render(request,'home.html',{'name':'Hishu'})

def add(request):
     a = int(request.POST['num1'])
     b = int(request.POST['num2'])
     c = a+b
     return render(request,'result.html', {'result' : c})
     
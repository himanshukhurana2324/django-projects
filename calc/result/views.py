from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'input.html', {'name':'Hishu'})

def calc(request):
    a = int(request.GET["val1"])
    b = int(request.GET["val2"])
    c = request.GET["operator"]
    res=0

    if(c=='+'):
        res = a+b
    elif(c=='-'):
        res = a-b
    elif(c=='*'):
        res = a*b
    elif(c=='/'):
        res = a/b
    else:
        res=" <! operator not defined !> "
    
    return render(request,'input.html',{'res':res})
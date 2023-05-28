from django.shortcuts import render

# Create your views here.
def if_con(request):
    a=10
    b=50
    d={'a':a,'b':b}
    return render(request,'if_con.html',d)

def twoif_con(request):
    a=10
    b=20
    c=30
    d={'a':a,'b':b,'c':c}
    return render(request,'twoif_con.html',d)

def ifelif_con(request):
    a,b,c=40,60,90
    d={'a':a,'b':b,'c':c}
    return render(request,'ifelif_con.html',d)
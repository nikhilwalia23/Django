from django.shortcuts import render
from django.http import HttpResponse
from .models import Combined_item
# Create your views here.

def index(request):
    a=Combined_item.objects.all()
    data=list()
    for i in a:
        data.append(i)
    context={'data':data}
    return render(request,"basic/index.html",context)
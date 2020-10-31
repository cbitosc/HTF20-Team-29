from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = "Hello"
    context = {'message':data}
    return render(request,'index.html',context)
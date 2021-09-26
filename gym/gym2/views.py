from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

from django.http.response import HttpResponseRedirect

from django.shortcuts import render
from .models import acc

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def formMessage(request):
    if request.method=='POST':
        sendmessege=acc()
        sendmessege.email=request.POST.get('email')
        sendmessege.address=request.POST.get('address')
        sendmessege.message=request.POST.get("message")
        sendmessege.name=request.POST.get('name')
        sendmessege.save()

        return HttpResponseRedirect('/')
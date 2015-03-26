from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    username = request.GET.get("username", "Anonymous")
    return render(request,"home.html", {
        "username": username
    })
    
def homeredirect(request):
    return redirect('home')
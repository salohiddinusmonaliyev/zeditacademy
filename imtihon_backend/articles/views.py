from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from articles.models import *


# Create your views here.
def articles(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(username=a, password=b)
        if user == None:
            return redirect('/login/')
        else:
            login(request, user)

    if request.user.is_authenticated:
        data = {
            "articles" : Article.objects.filter(author_id=request.user.id),
        }
        return render(request, "home.html", data)
    else:
        return redirect("/login/")


def detail(request, a):
    data = {
        "article" : Article.objects.get(id=a)
    }
    return render(request, "detail.html", data)

def login_a(request):
    return render(request, 'login.html')


def logout_a(request):
    logout(request)
    return redirect('/login/')


def addpost(request):
    return render(request, "new.html")


def new(request):
    title = request.POST.get("title")
    mavzu = request.POST.get("mavzu")
    text = request.POST.get("text")
    user = Users.objects.get(user=request.user)
    print(title, mavzu, text, user)
    Article.objects.create(title=title, mavzu=mavzu, text=text, author=user)
    return redirect("home")
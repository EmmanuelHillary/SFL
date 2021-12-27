from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def schedule(request):
    return render(request, "schedule.html")

def result(request):
    return render(request, "result.html")

def table(request):
    return render(request, "table.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def fpl(request):
    return render(request, "fpl.html")


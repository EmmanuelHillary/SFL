from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def schedule(request):
    return render(request, "schedule.html")

def result(request):
    return render(request, "result.html")

def table(request):
    return render(request, "table.html")


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from fantasy.models import UserFPLPick
from django.shortcuts import redirect, get_object_or_404


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

@login_required(login_url='/login/')
def fpl(request):
    return render(request, "fpl.html")

@login_required(login_url='/login/')
def create_team(request):
    return render(request, "create_team.html")

@login_required(login_url='/login/')
def pick_team(request):
    user = UserFPLPick.objects.filter(user__user__username=request.user.username)
    if not user.exists():
        return redirect("frontend:create_team")
    return render(request, "pick_team.html")

@login_required(login_url='/login/')
def transfer(request):
    return render(request, "transfer.html")

@login_required(login_url='/login/')
def points(request):
    return render(request, "points.html")

def logout_view(request):
    logout(request)
    return redirect('frontend:index')


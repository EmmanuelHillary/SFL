from django.urls import path
from .views import (index, schedule, result, table, login,
register, fpl, create_team, logout_view, pick_team, transfer, points)

app_name = "frontend"

urlpatterns = [
    path('', index, name="index"),
    path('fixtures/', schedule, name="schedule"),
    path('results/', result, name="result"),
    path('login/', login, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register, name="register"),
    path('fpl/', fpl, name="fpl"),
    path('fpl/transfer/', transfer, name="transfer"),
    path('fpl/create-team/', create_team, name="create_team"),
    path('fpl/pick-team/', pick_team, name="pick_team"), 
    path('fpl/points/', points, name="points"), 
]

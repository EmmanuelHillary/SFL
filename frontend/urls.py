from django.urls import path
from .views import index, schedule, result, table, login, register, fpl

app_name = "frontend"

urlpatterns = [
    path('', index, name="index"),
    path('fixtures/', schedule, name="schedule"),
    path('results/', result, name="result"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('fpl/', fpl, name="fpl"),
    # path('/table', table, name="table")
]

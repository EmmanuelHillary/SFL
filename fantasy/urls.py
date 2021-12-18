from django.urls import path
from .views import (UserFPLCreateAPIView, UserFPLSelectTeam, UserFPLSubTeam, UserFPLTransferTeam, 
UserFPLViewTeam, GameWeekPoints)

app_name="fantasy"

urlpatterns = [
    path('create/', UserFPLCreateAPIView.as_view(), name="create"),
    path('view-team/', UserFPLViewTeam.as_view(), name="view-team"),
    path('select-team/', UserFPLSelectTeam.as_view(), name="select-team"),
    path('gameweek-points/', GameWeekPoints.as_view(), name="gameweek-points"),
    path('transfer/<str:player>/<str:postion>/', UserFPLTransferTeam.as_view(), name="substitue"),
    path('substitute/<str:player>/<str:postion>/', UserFPLSubTeam.as_view(), name="substitue")
]

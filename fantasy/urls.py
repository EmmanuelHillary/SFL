from django.urls import path
from .views import (UserFPLCreateAPIView, UserFPLSelectTeam, UserFPLSubTeam, UserFPLTransferTeam, 
UserFPLViewTeam, GameWeekPoints, MakeCaptain, UserDetails, ChangeGameweek, CapBoolean)

app_name="fantasy"

urlpatterns = [
    path('create/', UserFPLCreateAPIView.as_view(), name="create"),
    path('view-team/', UserFPLViewTeam.as_view(), name="view-team"),
    path('select-team/', UserFPLSelectTeam.as_view(), name="select-team"),
    path('captain/<str:player>/', MakeCaptain.as_view(), name="captain"),
    path('cap/', CapBoolean.as_view(), name="cap"),
    path('gameweek-points/', GameWeekPoints.as_view(), name="gameweek-points"),
    path('user-points/', UserDetails.as_view(), name="user-points"),
    path('new-gameweek/', ChangeGameweek.as_view(), name="new-gameweek"),
    path('transfer/<str:player>/<str:position>/', UserFPLTransferTeam.as_view(), name="transfer"),
    path('substitute/<str:player>/<str:position>/', UserFPLSubTeam.as_view(), name="substitue"),
]

from django.urls import path
from .views import TableAPIView,GoalScorerAPIView,AssistAPIView, FixtureAPIView, ResultsAPIView

app_name = "league"

urlpatterns = [
    path('standings/', TableAPIView.as_view(), name="standing"),
    path('goalscorer/', GoalScorerAPIView().as_view(), name="goalscorer"),
    path('assist/', AssistAPIView().as_view(), name="assist"),
    path('fixture/', FixtureAPIView().as_view(), name="fixture"),
    path('results/', ResultsAPIView().as_view(), name="results"),
]

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Team,Player,GameweekFixtures
from .serializers import TableSerializer,TopScorerSerializer,TopAssistSerializer,GameweekFixturesSerializer

class TableAPIView(ListAPIView):
    queryset = Team.objects.all().order_by("-total_points")
    serializer_class = TableSerializer
class GoalScorerAPIView(ListAPIView):
    queryset=Player.objects.all().order_by("-total_goal_scored")
    serializer_class=TopScorerSerializer
class AssistAPIView(ListAPIView):
    queryset=Player.objects.all().order_by("-total_assists")
    serializer_class=TopAssistSerializer
class ResultsAPIView(ListAPIView):
    queryset=GameweekFixtures.objects.all()
    serializer_class=GameweekFixturesSerializer
class FixtureAPIView(ListAPIView):
    queryset=GameweekFixtures.objects.all()
    serializer_class=GameweekFixturesSerializer
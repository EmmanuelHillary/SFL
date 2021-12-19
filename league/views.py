from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Team,Player,GameweekFixtures
from rest_framework.permissions import AllowAny
from .serializers import TableSerializer,TopScorerSerializer,TopAssistSerializer,GameweekFixturesSerializer

class TableAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Team.objects.all().order_by("-total_points")
    serializer_class = TableSerializer
class GoalScorerAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset=Player.objects.all().order_by("-total_goal_scored")
    serializer_class=TopScorerSerializer
class AssistAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset=Player.objects.all().order_by("-total_assists")
    serializer_class=TopAssistSerializer
class ResultsAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset=GameweekFixtures.objects.all()
    serializer_class=GameweekFixturesSerializer
class FixtureAPIView(ListAPIView): 
    permission_classes = [AllowAny]
    queryset=GameweekFixtures.objects.all()
    serializer_class=GameweekFixturesSerializer
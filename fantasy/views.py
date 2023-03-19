from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import UserFPLCreate, UserFPLPick, UserProfile, Captain, Cap
from .serializers import UserFPLCreateSerializer, UserViewTeamSerializer, UserProfileSerializer
from league.serializers import PlayerSerializer
from league.models import GameweekName
from rest_framework.views import APIView
from league.models import Player
from rest_framework.response import Response
from rest_framework import status
import math
from rest_framework import permissions


class UserFPLCreateAPIView(generics.CreateAPIView):
    queryset = UserFPLCreate.objects.all()
    serializer_class = UserFPLCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=UserProfile.objects.get(user=self.request.user))
    

class UserFPLSelectTeam(APIView):
    def get(self, request, *args, **kwargs):
        goalkeeper = Player.objects.filter(position__name_short="GKP")
        defenders = Player.objects.filter(position__name_short="DEF")
        midfielders = Player.objects.filter(position__name_short="MFS")
        attackers = Player.objects.filter(position__name_short="ATT")
        data = {
            'gkp': PlayerSerializer(goalkeeper, many=True).data,
            'def': PlayerSerializer(defenders, many=True).data,
            'mid': PlayerSerializer(midfielders, many=True).data,
            'att': PlayerSerializer(attackers, many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)

class UserFPLSubTeam(APIView):
    def get(self, request, *args, **kwargs):
        user = UserFPLPick.objects.filter(user__user__username=request.user.username)
        if user.exists():
            user = user.first()
            player_postion = self.kwargs["position"]
            if player_postion == "gkp":
                player_to_bench  = self.kwargs["player"]
                player_to_team = user.gkp_bench 
                user.gkp = player_to_team
                user.save()
                user.gkp_bench = Player.objects.get(name=player_to_bench)
                user.save()
            if player_postion == "def":
                player_to_team = user.def_bench 
                player_to_bench  = self.kwargs["player"]
                if user.def1.name == player_to_bench:
                    user.def1 = player_to_team
                    user.save()
                if user.def2.name == player_to_bench:
                    user.def2 = player_to_team
                    user.save()
                if user.def3.name == player_to_bench:
                    user.def3 = player_to_team
                    user.save()
                if user.def4.name == player_to_bench:
                    user.def4 = player_to_team
                    user.save()
                user.def_bench  = Player.objects.get(name=player_to_bench)
                user.save()
            if player_postion == "mid":
                player_to_team = user.mid_bench 
                player_to_bench  = self.kwargs["player"]
                if user.mid1.name == player_to_bench:
                    user.mid1 = player_to_team
                    user.save()
                if user.mid2.name == player_to_bench:
                    user.mid2 = player_to_team
                    user.save()
                if user.mid3.name == player_to_bench:
                    user.mid3 = player_to_team
                    user.save()
                user.mid_bench  = Player.objects.get(name=player_to_bench)
                user.save()
            if player_postion == "att":
                player_to_team = user.att_bench 
                player_to_bench  = self.kwargs["player"]
                if user.att1.name == player_to_bench:
                    user.att1 = player_to_team
                    user.save()
                if user.att2.name == player_to_bench:
                    user.att2 = player_to_team
                    user.save()
                if user.att3.name == player_to_bench:
                    user.att3 = player_to_team
                    user.save()
                user.att_bench  = Player.objects.get(name=player_to_bench)
                user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserFPLViewTeam(RetrieveAPIView):
    queryset = UserFPLPick.objects.all()
    serializer_class = UserViewTeamSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user__user__username=self.request.user.username)
        self.check_object_permissions(self.request, obj)
        return obj

class UserFPLTransferTeam(APIView):
    def get(self, request, *args, **kwargs):
        user = UserFPLPick.objects.filter(user__user__username=request.user.username)
        if user.exists():
            user = user.first()
            postion = self.kwargs["position"]
            if postion == "gkp":
                player_to_transfer  = self.kwargs["player"]
                user.gkp =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "gkp_bench":
                player_to_transfer  = self.kwargs["player"]
                user.gkp_bench =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "def1":
                player_to_transfer  = self.kwargs["player"]
                user.def1 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "def2":
                player_to_transfer  = self.kwargs["player"]
                user.def2 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "def3":
                player_to_transfer  = self.kwargs["player"]
                user.def3 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "def4":
                player_to_transfer  = self.kwargs["player"]
                user.def4 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "def_bench":
                player_to_transfer  = self.kwargs["player"]
                user.def_bench =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "mid1":
                player_to_transfer  = self.kwargs["player"]
                user.mid1 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "mid2":
                player_to_transfer  = self.kwargs["player"]
                user.mid2 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "mid3":
                player_to_transfer  = self.kwargs["player"]
                user.mid3 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "mid_bench":
                player_to_transfer  = self.kwargs["player"]
                user.mid_bench =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "att1":
                player_to_transfer  = self.kwargs["player"]
                user.att1 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "att2":
                player_to_transfer  = self.kwargs["player"]
                user.att2 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "att3":
                player_to_transfer  = self.kwargs["player"]
                user.att3 =  Player.objects.get(name=player_to_transfer)
                user.save()
            if postion == "att_bench":
                player_to_transfer  = self.kwargs["player"]
                user.att_bench =  Player.objects.get(name=player_to_transfer)
                user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class MakeCaptain(APIView):
    def get(self, request, *args, **kwargs):
        player_to_captain = self.kwargs.get("player")
        user = UserProfile.objects.get(user__username=request.user.username)
        team_obj = UserFPLPick.objects.get(user=user)
        team = [
            team_obj.gkp,
            team_obj.def1, 
            team_obj.def2,
            team_obj.def3,
            team_obj.def4,
            team_obj.mid1,
            team_obj.mid2,
            team_obj.mid3,
            team_obj.att1,
            team_obj.att2,
            team_obj.att3,
            ]
        for i in team:
            if i.name == player_to_captain: 
                captain, created = Captain.objects.get_or_create(user=user)
                captain.captain = Player.objects.get(name=player_to_captain)
                captain.save()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
            
        


class GameWeekPoints(APIView):
    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.filter(user__username=request.user.username)
        gw_tem_points = UserFPLPick.objects.get(user=user)
        gw_tem_points.gkp.sfl_gw_point
        captain = Captain.objects.get(user=user)
        return Response({"data": {
            "gkp_points": gw_tem_points.gkp.sfl_gw_point,
            "def1_points": gw_tem_points.def1.sfl_gw_point,
            "def2_points": gw_tem_points.def2.sfl_gw_point,
            "def3_points": gw_tem_points.def3.sfl_gw_point,
            "def4_points": gw_tem_points.def4.sfl_gw_point,
            "mid1_points": gw_tem_points.mid1.sfl_gw_point,
            "mid2_points": gw_tem_points.mid2.sfl_gw_point,
            "mid3_points": gw_tem_points.mid3.sfl_gw_point,
            "att1_points": gw_tem_points.att1.sfl_gw_point,
            "att2_points": gw_tem_points.att2.sfl_gw_point,
            "att3_points": gw_tem_points.att3.sfl_gw_point,
            "gkp_bench_points": gw_tem_points.gkp_bench.sfl_gw_point,
            "def_bench_points": gw_tem_points.def_bench.sfl_gw_point,
            "mid_bench_points": gw_tem_points.mid_bench.sfl_gw_point,
            "att_bench_points": gw_tem_points.att_bench.sfl_gw_point,
            "captain": captain.captain.sfl_gw_point
        }})

class UserDetails(APIView):
    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.filter(user__username=request.user.username).first()
        users_teams = UserProfile.objects.all().order_by('-total_points')
        total_teams = UserProfile.objects.all().count()
        total_team_gw_points = 0
        for team in users_teams:
            total_team_gw_points += team.gw_points
        average_points = math.ceil(total_team_gw_points / total_teams)
        user_gw_points = user.gw_points
        user_total_points = user.total_points
        highest_points = UserProfile.objects.all().order_by('-gw_points').first().gw_points
        user_rank = UserProfileSerializer(users_teams, many=True).data 
        data = {
            "average_points" : average_points,
            "user_gw_points" : user_gw_points, 
            "highest_points" : highest_points,
            "user_total_points": user_total_points,
            "user_rank" : user_rank,
        }
        return Response(data, status=status.HTTP_200_OK)

class ChangeGameweek(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        teams = UserFPLPick.objects.all()
        players = Player.objects.all()
        for i in teams:
            i.gameweek = GameweekName.objects.filter(id__gt=i.gameweek.id).order_by('id').first()
            i.save()
            i.user.total_points += i.user.gw_points
            i.user.save()
            i.user.gw_points = 0
            i.user.save()
        for i in players:
            i.sfl_total_points += i.sfl_gw_point
            i.save()
            i.total_goal_scored += i.sfl_gw_goals
            i.save()
            i.sfl_gw_goals= 0
            i.save()
            i.total_assists += i.sfl_gw_assists
            i.save()
            i.sfl_gw_assists = 0
            i.save()
            i.sfl_gw_point = 0
            i.save() 
        return Response(status=status.HTTP_200_OK)
    
class UpdateGWPoints(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        teams = UserFPLPick.objects.all()
        for i in teams:
            captain = Captain.objects.get(user=i.user)
            team = [
            i.gkp,
            i.def1, 
            i.def2,
            i.def3,
            i.def4,
            i.mid1,
            i.mid2,
            i.mid3,
            i.att1,
            i.att2,
            i.att3,
            ]
            total_gw_points = 0   
            for j in team:
                if j == captain.captain:
                    total_gw_points += j.sfl_gw_point * 2
                else:
                    total_gw_points += j.sfl_gw_point
            i.user.gw_points = total_gw_points
            i.user.save()
        return Response(status=status.HTTP_200_OK)

class CapBoolean(APIView):
    def get(self, request, *args, **kwargs):
        cap = Cap.objects.all().first()
        data = {
            "cap": cap.cap
        }
        return Response(data, status=status.HTTP_200_OK)
        






    

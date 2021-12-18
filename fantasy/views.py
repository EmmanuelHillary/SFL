from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import UserFPLCreate, UserFPLPick, UserProfile, Captain
from .serializers import UserFPLCreateSerializer, UserViewTeamSerializer
from league.serializers import PlayerSerializer
from rest_framework.views import APIView
from league.models import Player
from rest_framework.response import Response
from rest_framework import status


class UserFPLCreateAPIView(generics.CreateAPIView):
    queryset = UserFPLCreate.objects.all()
    serializer_class = UserFPLCreateSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=UserProfile.objects.get(user=self.request.user))
    

class UserFPLSelectTeam(APIView):
    def get(self, request, *args, **kwargs):
        goalkeeper = Players.objects.filter(position__name_short="GKP")
        defenders = Players.objects.filter(position__name_short="DEF")
        midfielders = Players.objects.filter(position__name_short="MFS")
        attackers = Players.objects.filter(position__name_short="ATT")
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
            player_postion = self.kwargs["postion"]
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
                    user.def1 = player_to_team
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


class UserFPLTransferTeam(APIView):
    def get(self, request, *args, **kwargs):
        user = UserFPLPick.objects.filter(user__user__username=request.user.username)
        if user.exists():
            user = user.first()
            postion = self.kwargs["postion"]
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
        user = UserProfile.objects.filter(user__username=request.user.username)
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
                captain = Captain.objects.get(user=user)
                if captain is not None:
                    captain.captain = Player.objects.get(name=player_to_captain)
                    captain.save()
                else:
                    captain = Captain.objects.create(
                    user=user,
                    captain=Player.objects.get(name=player_to_captain),
                    )
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
            "captain": captain.captain.sfl_gw_point * 2
        }})

class UserDetails(APIView):
    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.filter(user__username=request.user.username).first()
        user_team = UserFPLPick.objects.get(user=user)
        user.total_points = 0
        gw_points = 0
        average_point = 0
        highest_points = 0



    

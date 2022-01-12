from rest_framework import serializers
from .models import Team,Player,Fixture, GameweekName, GameweekFixtures
    

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            "name",
            "wins",
            "losses",
            "gf",
            "ga",
            "total_points"
        ]


class TopScorerSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Player
        fields=[
            "name",
            "team",
            "total_goal_scored"
        ]
    def get_team(self, obj):
        return obj.team.name
        
class TopAssistSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Player
        fields=[
            "name",
            "team",
            "total_assists"
        ]
    def get_team(self, obj):
        return obj.team.name

class FixtureSerializer(serializers.ModelSerializer):
    home_team = serializers.SerializerMethodField(read_only=True)
    away_team = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Fixture
        fields=[
            "home_team",
            "home_team_score",
            "away_team",
            "away_team_score",
            "is_started"
        ]
    def get_home_team(self, obj):
        return obj.home_team.name
    def get_away_team(self, obj):
        return obj.away_team.name

class GameweekFixturesSerializer(serializers.ModelSerializer):
    fixtures = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=GameweekFixtures
        fields=[
            "fixtures"
        ]
    def get_fixtures(self, obj):
        gameweekfixtures = {}
        fixtures = [FixtureSerializer(obj.fx1).data, FixtureSerializer(obj.fx2).data]
        gameweekfixtures[obj.gw.name] = fixtures
        return gameweekfixtures

class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField(read_only=True)
    position = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Player
        fields = [
            'id',
            'name',
            'team',
            'position',
            'sfl_price',
            'sfl_gw_point',
            'sfl_total_points',
        ]
    def get_team(self, obj):
        return obj.team.name
    
    def get_position(self, obj):
        return obj.position.name
        
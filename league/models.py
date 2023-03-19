from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    total_points = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    ga = models.PositiveIntegerField(default=0)
    gf = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Fixture(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_team",on_delete=models.CASCADE)
    home_team_score = models.PositiveIntegerField(default=0)
    away_team = models.ForeignKey(Team, related_name="away_team",on_delete=models.CASCADE)
    away_team_score = models.PositiveIntegerField(default=0)
    is_started = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.home_team.name} {self.home_team_score} v {self.away_team_score} {self.away_team.name}'
    

class Position(models.Model):
    name = models.CharField(max_length=16)
    name_short = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, related_name="player_team", on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    total_goal_scored = models.PositiveIntegerField(default=0)
    total_assists = models.PositiveIntegerField(default=0)
    sfl_price = models.PositiveIntegerField(default=0)
    sfl_gw_point = models.PositiveIntegerField(default=0)
    sfl_total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

class GameweekName(models.Model):
    name = models.CharField(max_length=16)
    def __str__(self):
        return self.name

class GameweekFixtures(models.Model):
    gw = models.ForeignKey(GameweekName, related_name="gameweek", on_delete=models.CASCADE)
    fx1 = models.ForeignKey(Fixture, related_name="fixture_1", on_delete=models.CASCADE)
    fx2 = models.ForeignKey(Fixture, related_name="fixture_2", on_delete=models.CASCADE)
    fx3 = models.ForeignKey(Fixture, related_name="fixture_3", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.gw.name
    
    class Meta:
        verbose_name_plural = "GameweekFixtures"


    


# class GoalScorerFixture(models.Model):
#     fixture = models.ForeignKey(Fixture, related_name="fixture_scores", on_delete=models.CASCADE)
#     player = models.ForeignKey(Player, related_name="goal_scorer", on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{'
    


    

    

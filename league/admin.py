from django.contrib import admin
from .models import Team, Fixture, Position, Player, GameweekName, GameweekFixtures


admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Position)
admin.site.register(Player)
admin.site.register(GameweekName)
admin.site.register(GameweekFixtures)

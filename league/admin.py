from django.contrib import admin
from .models import Team, Fixture, Position, Player, GameweekName, GameweekFixtures


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'sfl_gw_point', 'sfl_gw_goals', 'sfl_gw_assists', 'sfl_total_points', 'total_goal_scored', 'total_assists')
    list_editable = ('sfl_gw_point', 'sfl_gw_goals', 'sfl_gw_assists')
    search_fields = ['name',]

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 0
    list_display = ('name', 'team', 'sfl_gw_point', 'sfl_gw_goals', 'sfl_gw_assists', 'sfl_total_points', 'total_goal_scored', 'total_assists')
    list_editable = ('sfl_gw_point', 'sfl_gw_goals', 'sfl_gw_assists')
    search_fields = ['name',]

class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]
    search_fields = ['name',]


admin.site.register(Team, TeamAdmin)
admin.site.register(Fixture)
admin.site.register(Position)
admin.site.register(Player, PlayerAdmin)
admin.site.register(GameweekName)
admin.site.register(GameweekFixtures)

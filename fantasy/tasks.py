from celery import shared_task
from .models import UserFPLPick, Captain
import schedule
import time

# @shared_task

def update_fpl():
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
    return None

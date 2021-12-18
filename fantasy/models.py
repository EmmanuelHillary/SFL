from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from league.models import Player, GameweekName


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    gw_points = models.PositiveIntegerField(default=0)
    total_points = models.PositiveIntegerField(default=0)
    bank = models.PositiveIntegerField(default=100)
    transfers = models.PositiveIntegerField(default=2)

    def __str__(self):
        return self.user.username 

class UserFPLCreate(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    gkp1 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_gkp1')
    gkp2 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_gkp2')
    def1 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_def1')
    def2 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_def2')
    def3 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_def3')
    def4 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_def4')
    def5 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_def5')
    mid1 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_mid1')
    mid2 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_mid2')
    mid3 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_mid3')
    mid4 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_mid4')
    att1 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_att1')
    att2 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_att2')
    att3 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_att3')
    att4 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='fpl_create_att4')

    def __str__(self):
        return self.user.user.username

class UserFPLPick(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='user_fpl_pick')
    gameweek = models.ForeignKey(GameweekName, on_delete=models.CASCADE, default=1)
    gkp = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='gkp')
    def1 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='def1')
    def2 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='def2')
    def3 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='def3')
    def4 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='def4')
    mid1 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='mid1')
    mid2 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='mid2')
    mid3 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='mid3')
    att1 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='att1')
    att2 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='att2')
    att3 = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='att3')
    gkp_bench = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='gkp_bench')
    def_bench = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='def_bench')
    mid_bench = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='mid_bench')
    att_bench = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='att_bench')

    def __str__(self):
        return self.user.user.username 
    

class Captain(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    captain = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='captain')

    def __str__(self):
        return f'{self.user.user.username} | captain: {self.captain.name}'
    


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


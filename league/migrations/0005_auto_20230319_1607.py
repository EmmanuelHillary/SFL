# Generated by Django 3.2 on 2023-03-19 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_gameweekfixtures_fx3'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='sfl_gw_assists',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='sfl_gw_goals',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

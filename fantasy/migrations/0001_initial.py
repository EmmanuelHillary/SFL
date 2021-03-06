# Generated by Django 3.2 on 2021-11-22 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('league', '0002_auto_20211119_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gw_points', models.PositiveIntegerField(default=0)),
                ('total_points', models.PositiveIntegerField(default=0)),
                ('bank', models.PositiveIntegerField(default=100)),
                ('transfers', models.PositiveIntegerField(default=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFPLPick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='att1', to='league.player')),
                ('att2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='att2', to='league.player')),
                ('att3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='att3', to='league.player')),
                ('att_bench', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='att_bench', to='league.player')),
                ('def1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='def1', to='league.player')),
                ('def2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='def2', to='league.player')),
                ('def3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='def3', to='league.player')),
                ('def4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='def4', to='league.player')),
                ('def_bench', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='def_bench', to='league.player')),
                ('gkp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gkp', to='league.player')),
                ('gkp_bench', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gkp_bench', to='league.player')),
                ('mid1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mid1', to='league.player')),
                ('mid2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mid2', to='league.player')),
                ('mid3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mid3', to='league.player')),
                ('mid_bench', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mid_bench', to='league.player')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_fpl_pick', to='fantasy.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='UserFPLCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_att1', to='league.player')),
                ('att2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_att2', to='league.player')),
                ('att3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_att3', to='league.player')),
                ('att4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_att4', to='league.player')),
                ('def1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_def1', to='league.player')),
                ('def2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_def2', to='league.player')),
                ('def3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_def3', to='league.player')),
                ('def4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_def4', to='league.player')),
                ('def5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_def5', to='league.player')),
                ('gkp1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_gkp1', to='league.player')),
                ('gkp2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_gkp2', to='league.player')),
                ('mid1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_mid1', to='league.player')),
                ('mid2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_mid2', to='league.player')),
                ('mid3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_mid3', to='league.player')),
                ('mid4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl_create_mid4', to='league.player')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Captain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='captain', to='league.player')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.userprofile')),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2024-01-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_games_is_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='first_team_result',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='نتیجه تیم اول'),
        ),
        migrations.AlterField(
            model_name='games',
            name='second_team_result',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='نتیجه تیم دوم'),
        ),
    ]

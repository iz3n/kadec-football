# Generated by Django 4.2.2 on 2024-01-11 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_userform_first_team_alter_userform_second_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinnerResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('reason', models.CharField(max_length=20)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.games')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile')),
            ],
        ),
    ]

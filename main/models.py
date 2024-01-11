from django.db import models
from django_jalali.db import models as jmodels



# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=15, verbose_name='شماره همراه')
    department = models.CharField(max_length=30, verbose_name='نام دپارتمان')
    user_token = models.CharField(max_length=30, verbose_name='توکن دسترسی')
    join_date = jmodels.jDateTimeField(verbose_name='تاریخ ثبت نام', auto_now_add=True)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Seassons(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان فصل')

    def __str__(self):
        return self.title

class Teams(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان تیم')
    img = models.FileField(null=True, blank=True, upload_to='media')
    def __str__(self):
        return self.title

class Games(models.Model):
    date_time = jmodels.jDateTimeField(verbose_name='تاریخ و زمان شروع')
    seasson = models.ForeignKey(Seassons, on_delete=models.CASCADE, verbose_name='انتخاب فصل', null=True, blank=True)
    first_team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name='تیم اول')
    second_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='Team_B', verbose_name='تیم دوم')
    first_team_result = models.IntegerField(default=0, verbose_name='نتیجه تیم اول', null=True, blank=True)
    second_team_result = models.IntegerField(default=0, verbose_name='نتیجه تیم دوم', null=True, blank=True)
    winner = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='winner', verbose_name='برنده بازی', null=True, blank=True)
    is_enable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.first_team.title + '--' + self.second_team.title


class UserForm(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    first_team = models.IntegerField(default=0,null=True, blank=True)
    second_team = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.user.name
    

class WinnerResult(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    score = models.IntegerField()
    reason = models.CharField(max_length=20)

    def __str__(self):
        return self.user.name
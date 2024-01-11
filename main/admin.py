from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Seassons)
admin.site.register(Teams)
admin.site.register(Games)
admin.site.register(UserForm)
from django.contrib import admin
from body.models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'user','user_type')

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'name', 'phone', 'age', 'gender','experience','skills')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'trainer', 'phone', 'age', 'gender', 'height', 'weight')

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

class SessionAdmin(admin.ModelAdmin):
    list_display = ('member', 'trainer', 'name', 'date', 'time','duration')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Session, SessionAdmin)

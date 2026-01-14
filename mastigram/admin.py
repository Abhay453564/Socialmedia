from django.contrib import admin
from .models import *

# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ('description','image','created_at')

admin.site.register(Post,AdminPost)

class AdminReel(admin.ModelAdmin):
    list_display = ('caption','reel','created_at')

admin.site.register(Reel,AdminReel)

class AdminVideo(admin.ModelAdmin):
    list_display = ('title','v_description','video','created_at')

admin.site.register(Video,AdminVideo)

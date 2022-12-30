from django.contrib import admin

from .forms import ProfileForm
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'user', 'username')
    form = ProfileForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')

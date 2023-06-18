from django.contrib import admin
from .models import Profile, Post
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]

# remove the default user setting and replace with custom ones
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post)

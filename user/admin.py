from django.contrib import admin
from .models import User, CustomUser, Agent, UserProfile

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_superuser',
        'is_organisor',
        'is_agent'
    ]
    class Meta:
        model = User
admin.site.register(User, UserAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'age',
        'agent',
        'organisation'
    ]
    class Meta:
        model = CustomUser
admin.site.register(CustomUser, CustomUserAdmin)

class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user'
    ]
    class Meta:
        model = Agent
admin.site.register(Agent, AgentAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user'
    ]
    class Meta:
        model = UserProfile
admin.site.register(UserProfile, UserProfileAdmin)
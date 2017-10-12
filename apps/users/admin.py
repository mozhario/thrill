from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User, UserSubscription, UserPost
from django.contrib.auth.models import Permission

from .forms import CustomUserAdmin


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserSubscription)
admin.site.register(Permission)
admin.site.register(UserPost)
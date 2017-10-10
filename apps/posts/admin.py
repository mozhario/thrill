from django.contrib import admin
from .models import UserPost, CommunityPost


admin.site.register(UserPost)
admin.site.register(CommunityPost)
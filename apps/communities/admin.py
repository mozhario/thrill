from .models import Community, CommunityPost

from apps.admin_site.admin import admin_site

admin_site.register(Community)
admin_site.register(CommunityPost)
from .models import User, UserSubscription, UserPost
from django.contrib.auth.models import Permission

from .forms import CustomUserAdmin
from apps.admin_site.admin import admin_site


admin_site.register(User, CustomUserAdmin)
admin_site.register(UserSubscription)
admin_site.register(Permission)
admin_site.register(UserPost)
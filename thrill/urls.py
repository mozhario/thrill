"""thrill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from apps.users.views import UserRegistrationView
from apps.users.forms import UserRegistrationForm

from . import settings
from apps.admin_site.admin import admin_site


urlpatterns = [
    url(r'^admin/', admin_site.urls),

    # Registration (django-registration)
    url(r'^accounts/register/$', UserRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'', include('apps.users.urls')),
    url(r'', include('apps.communities.urls')),
    url(r'', include('apps.comments.urls')),
    url(r'', include('apps.chat.urls')),
    url(r'', include('apps.likes.urls')),

    url(r'^api_v1/', include('apps.api_v1.urls')),

    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    # staticfiles_urlpatterns(),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
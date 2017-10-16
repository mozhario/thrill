from django.forms import ModelForm

from .models import Community


class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = [
            'title',
            'short_link',
            'description',
            'avatar_pic',
        ]
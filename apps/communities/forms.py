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

    def is_valid(self):
        valid = super(CommunityForm, self).is_valid()
        short_link = self.cleaned_data.get('short_link', None)
        if short_link:
            communities = Community.objects.filter(short_link=short_link)
            if communities:
                valid = False
                self._errors['not_unique_short_link'] = "Community with such short link already exist."
        
        return valid

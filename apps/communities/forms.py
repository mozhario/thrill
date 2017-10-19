from django.forms import ModelForm

from .models import Community, CommunityPost


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


class CommunityPostForm(ModelForm):
    class Meta:
        model = CommunityPost
        fields = [
            'title',
            'content',
            'excerpt',
            'thumbnail'
        ]

    def is_valid(self):
        valid = super(CommunityPostForm, self).is_valid()
        
        filled_correctly = False

        if self.cleaned_data['thumbnail'] or self.cleaned_data['content']:
            filled_correctly = True
        
        return valid and filled_correctly
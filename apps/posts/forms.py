from django.forms import ModelForm
from .models import UserPost, CommunityPost


class PostCreationForm(ModelForm):
	class Meta:
		fields = (
		    'title',
		    'content',
		    'excerpt',
		    'thumbnail'
		)


class UserPostCreationForm(PostCreationForm):
	class Meta:
		model = UserPost


class CommunityPostCreationForm(PostCreationForm):
	class Meta:
		model = CommunityPost
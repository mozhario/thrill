from datetime import datetime

from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.admin import UserAdmin
from registration.forms import RegistrationForm

from .models import User, UserPost


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'birth_date',
            'bio',
            'profile_pic',
            'email',
            'phone',
            'location'
        )
        widgets = {
            'birth_date': SelectDateWidget(years=range(datetime.today().year, 1900, -1))
        }


class UserRegistrationForm(RegistrationForm):
    """
    User register form overriden to add some custom
    user model fields.
    """

    class Meta:
        model = User
        fields = (
        	'first_name',
        	'last_name',
            'birth_date',
            'profile_pic',
        	'username',
        	'email',
            'location'
        )
        widgets = {
            'birth_date': SelectDateWidget(years=range(datetime.today().year, 1900, -1))
        }


class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('profile_pic', 'birth_date', 'location', 'bio', 'phone')}),
    )


class UserPostForm(ModelForm):
    class Meta:
        model = UserPost
        fields = [
            'title',
            'content',
            'excerpt',
            'thumbnail'
        ]

    def is_valid(self):
        valid = super(UserPostForm, self).is_valid()
        
        filled_correctly = False

        if self.cleaned_data['thumbnail'] or self.cleaned_data['content']:
            filled_correctly = True
        
        return valid and filled_correctly
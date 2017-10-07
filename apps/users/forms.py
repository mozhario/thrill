from datetime import datetime

from registration.forms import RegistrationForm
from django.contrib.auth.models import Group
#from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget

from .models import User


class UserForm(RegistrationForm):
    '''
    User register form overriden to add some custom
    user model fields and add user to default group 
    when saving
    '''

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

    def save(self, commit=True, *args, **kwargs):
        user = super(UserForm, self).save(commit=False, *args, **kwargs)

        if commit:
            group = Group.objects.get(name='User')
            # FIXME: doesn't create a relation for some reason
            user.groups.add(group)
            user.save()

        return user
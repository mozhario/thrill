from datetime import datetime

from registration.forms import RegistrationForm
from django.forms.extras.widgets import SelectDateWidget

from .models import User


class UserForm(RegistrationForm):
    '''
    User register form overriden to add some custom
    user model fields.
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
        
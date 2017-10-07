from registration.forms import RegistrationForm
from django.contrib.auth.models import Group

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
        	'username',
        	'email',
        )

    def save(self, commit=True, *args, **kwargs):
        user = super(UserForm, self).save(commit=False, *args, **kwargs)

        if commit:
            group = Group.objects.get(name='User')
            # FIXME: doesn't create a relation for some reason
            user.groups.add(group)
            user.save()

        return user
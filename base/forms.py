from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import Room, User, Message


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio', 'avatar']


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email',
                  'password1', 'password2', 'bio', 'avatar']

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from todo.models import Task


#the register form
class CreateUserForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username', 'password1', 'password2']


#the login form

class LoginUserForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput)
    password=forms.CharField(widget=PasswordInput)

class TaskForm(forms.ModelForm):

    class Meta:
        model=Task
        fields='__all__'
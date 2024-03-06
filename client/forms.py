from django import forms
from .models import UserProfile,UserTask
from django.db import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserForm(UserCreationForm): 
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','email','password1', 'password2','phone','last_login']

# class UserAuthForm(AuthenticationForm): 
#     class Meta:
#         model = UserProfile
#         fields = ['email','password']
        
class UserTaskForm(forms.ModelForm):
    class Meta:
        model=UserTask
        fields=['title','description','date','status']

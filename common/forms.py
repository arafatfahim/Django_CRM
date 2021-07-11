from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Enter a Valid Email Address')
    class Meta:
        model = User
        fields =[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'address',
            'birthdate',
            'phone_number',
            'profile_img'
        ]
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# User Login Form

class UserLoginForm(forms.Form):
    
    """ Form to be used to log user in """
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# User Registraion Form

class UserRegistrationForm(UserCreationForm):
    
    """Form used to register a new user"""
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation2", 
        widget=forms.PasswordInput)
    
    """ Create an inner class. An inner class is a class that we can use that will 
provide some information about this form. These are called meta classes and 
Django usually uses them internally to determine things about the class. 
We can also use it to specify the model that we want to store information in;
and we want we want to use it to specify the fields that we're going to expose 
which is our email, username, password1 and password2. so I'm going to copy the
name of my user registration form here and gonna head over to my views.py """

    class Meta:
        
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        
        
        
        
        
        
        
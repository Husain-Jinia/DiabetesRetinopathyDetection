from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


#Form for user registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','age', 'email', 'password1', 'password2']

# Proxy form for user registration
class UserRegisterProxy(forms.Form):
    email = forms.EmailField()
    age = forms.IntegerField()
    bio = forms.Textarea()

    password1 = forms.CharField(max_length=256,required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=256,required=True,widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=256,required=True)
    last_name = forms.CharField(max_length=256,required=True)
    username = forms.CharField(max_length=256,required=True)
    # For saving & validating the form data into the database

    def save(self):   
        validated_data = self.cleaned_data
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password1'])
        profile = Profile.objects.create(
            age=validated_data['age'],
            bio=validated_data['bio'],
            user=user
        )
        user.save()
        profile.save()
    
    

#Form for updating user information
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

#form for updating user profile information
class ProfileUpdateForm(forms.ModelForm):
    age = forms.IntegerField()
    bio = forms.Textarea()
    class Meta:
        model = Profile
        fields = ['profile_picture','age','bio']
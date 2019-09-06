from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tutor

class UserSignUp_Form (UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # def save(self, commit = True):
    #     user = super(UserSignUp_Form, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user

class StudentSignUp_Form(forms.ModelForm):
    
    class Meta:
        model = Tutor
        fields = ("degree","identity_document","description","subjects")
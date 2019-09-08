from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tutor
from django.db import transaction

class UserSignUp_Form (UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name","last_name", "email", "password1", "password2")
    
    #@transaction.atomic
    def save(self, commit = True):
        user = super(UserSignUp_Form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_Tutor = True
        user.save()
        # description = self.cleaned_data.get('email')
        # student = Tutor.objects.create(user=user, description=description)
        # student.save()
        return user
    

class TutorSignUp_Form(forms.ModelForm):
    
    class Meta:
        model = Tutor
        fields = ("degree","identity_document","description","subjects")
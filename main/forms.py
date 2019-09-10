from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tutor, Student, College,Subject
from django.db import transaction

class UserSignUp_Form (UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","first_name","last_name", "email", "password1", "password2")
    
    # #@transaction.atomic
    def save(self, commit = True):
        user = super(UserSignUp_Form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.is_teacher = True
        user.save()
        return user
    

class TutorSignUp_Form(forms.ModelForm):    
    class Meta:
        model = Tutor
        fields = ("degree","identity_document","description","subjects")

    def save(self, commit=True):
        tutor = super().save(commit=commit)
        tutor.user.is_teacher = True
        tutor.save()
        return tutor

class StudentSignUp_Form(forms.ModelForm):
    college_id = forms.ModelChoiceField(queryset = College.objects.all())

    class Meta:
        model = Student
        fields = ("college_id",)

    def save(self, commit=True):
        student = super().save(commit=commit)
        student.user.is_student = True
        student.save()
        return student
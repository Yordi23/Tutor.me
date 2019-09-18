from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tutor, Student, College,Subject
from django.db import transaction

class UserSignUp_Form (UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","first_name","last_name", "email", "password1", "password2","phone")
    
    # #@transaction.atomic
    def save(self, commit = True):
        user = super(UserSignUp_Form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.is_teacher = True
        user.save()
        return user
    

class TutorSignUp_Form(forms.ModelForm):  
    #subjects = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Tutor
        fields = ("degree","identity_document","description","subjects")

    def save(self, user, commit=True):
        tutor = super(TutorSignUp_Form,self).save(commit=False)
        tutor.user = user
        tutor.user.is_teacher = True
        tutor.user.save()
        tutor.save()
        return tutor

class StudentSignUp_Form(forms.ModelForm):
    college_id = forms.ModelChoiceField(queryset = College.objects.all())

    class Meta:
        model = Student
        fields = ("college_id",)

    def save(self, user,commit=True):
        student = super(StudentSignUp_Form,self).save(commit=False)
        student.user = user
        student.user.is_student = True
        student.user.save()
        student.save()
        return student
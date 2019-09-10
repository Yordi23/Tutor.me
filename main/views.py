from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignUp_Form, TutorSignUp_Form, StudentSignUp_Form
from .models import Tutor, User, Subject, Student

# Create your views here.


def homepage(request):
    return render(request = request, template_name = "main/home.html")



def tutor_signup(request):
    # user_form = UserSignUp_Form
    # tutor_form = TutorSignUp_Form

    if request.method == 'POST':
        user_form = UserSignUp_Form(request.POST)        
        tutor_form = TutorSignUp_Form(request.POST)

        if user_form.is_valid() and tutor_form.is_valid() :
            user = user_form.save()
            
            tutor = Tutor.objects.create(user = user)
            tutor.degree = tutor_form.cleaned_data['degree']
            tutor.identity_document = tutor_form.cleaned_data['identity_document']
            tutor.description = tutor_form.cleaned_data['description']
            tutor.subjects.add(*tutor_form.cleaned_data['subjects'])
            #subjects = Subject.objects.create(tutor_form.cleaned_data['subjects'])
            #tutor.subjects.add = subjects
            tutor.save()
            tutor_form.save()
            #tutor_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('main:homepage')
        else:
            return HttpResponse("Not valid") 

    user_form = UserSignUp_Form
    tutor_form = TutorSignUp_Form

    return render (request, "main/tutor_signup.html", context={"user_form":user_form,"tutor_form":tutor_form})


def student_signup(request):
    # user_form = UserSignUp_Form
    # tutor_form = TutorSignUp_Form

    if request.method == 'POST':
        user_form = UserSignUp_Form(request.POST)        
        student_form = StudentSignUp_Form(request.POST)

        if user_form.is_valid() and student_form.is_valid() :
            user = user_form.save()
            
            student = Student.objects.create(user = user)
            student.college_id = student_form.cleaned_data['college_id']
            student.save()
  
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('main:homepage')
        else:
            return HttpResponse("Not valid") 

    user_form = UserSignUp_Form
    student_form = StudentSignUp_Form

    return render (request, "main/student_signup.html", context={"user_form":user_form,"student_form":student_form})

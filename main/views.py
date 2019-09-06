from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserSignUp_Form, StudentSignUp_Form

# Create your views here.

def homepage(request):
    user_form = UserSignUp_Form
    student_form = StudentSignUp_Form

    return render (request, "main/student_signup.html", context={"user_form":user_form,"student_form":student_form})
    #return render(request = request, template_name = "main/student_signup.html")
    #
# def homepage(request):
#     return render(request = request, template_name = "main/home.html")
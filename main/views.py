from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm

# Create your views here.

def homepage(request):
    form = NewUserForm

    return render (request, "main/student_signup.html", context={"form":form})
    #return render(request = request, template_name = "main/student_signup.html")

# def homepage(request):
#     return render(request = request, template_name = "main/home.html")
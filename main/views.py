from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignUp_Form, TutorSignUp_Form, StudentSignUp_Form
from .models import Tutor, User, Subject, Student, User_Request
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


# def homepage(request):
#     return render(request = request, template_name = "main/home.html")

def homepage_tutor(request):
    user_id = None
   
    if request.user.is_authenticated:
        user_id = request.user.id

    user_requests = User_Request.objects.filter(tutor_ID_id=user_id)
    students = []
    for user_request in user_requests:
        students.append(Student.objects.get(user = user_request.student_ID_id))

    return render(request = request, template_name = "main/homepage_tutor.html", context={"students":students})

def homepage_student(request):
    return render(request = request, template_name = "main/homepage_student.html", context={"tutors":Tutor.objects.all()})



def tutor_signup(request):

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
            tutor.save()
            tutor_form.save(user)
            messages.success(request, f"Nueva cuenta registrada exitosamente")

            login(request, user)
            #messages.success(request, _('Your profile was successfully updated!'))
            return homepage_tutor(request)  #redirect("main:homepage_tutor")
        else:
            messages.warning(request, "Datos inválidos")

    user_form = UserSignUp_Form
    tutor_form = TutorSignUp_Form

    return render (request, "main/tutor_signup.html", context={"user_form":user_form,"tutor_form":tutor_form})


def student_signup(request):

    if request.method == 'POST':
        user_form = UserSignUp_Form(request.POST)        
        student_form = StudentSignUp_Form(request.POST)

        if user_form.is_valid() and student_form.is_valid() :
            user = user_form.save()
            
            student = Student.objects.create(user = user)
            student.college_id = student_form.cleaned_data['college_id']
            student.save()
            student_form.save(user)
            messages.success(request, f"Nueva cuenta registrada exitosamente")

            login(request, user)
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect("main:homepage_student")
        else:
            messages.warning(request, "Datos inválidos")

    user_form = UserSignUp_Form
    student_form = StudentSignUp_Form

    return render (request, "main/student_signup.html", context={"user_form":user_form,"student_form":student_form})


def homepage (request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Acaba de iniciar sesión como: {user.username}")
                if(user.is_teacher):
                    return  homepage_tutor(request)  #redirect("main:homepage_tutor")
                elif(user.is_student):
                    return redirect("main:homepage_student")
            else:
                messages.error(request, "Nombre de usuario o contraseña inválido")
        else:
           messages.error(request, "Nombre de usuario o contraseña inválido")

    form = AuthenticationForm()
    return render(request, "main/home.html", {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def requests_student(request):
    user_id = None
   
    if request.user.is_authenticated:
        user_id = request.user.id

    pending_user_requests = User_Request.objects.filter(student_ID_id=user_id,status='P')
    accepted_user_requests = User_Request.objects.filter(student_ID_id=user_id,status='A')
    pending_tutors = []
    accepted_tutors = []

    for user_request in pending_user_requests:
        pending_tutors.append(Tutor.objects.get(user = user_request.tutor_ID_id))
    
    for user_request in accepted_user_requests:
        accepted_tutors.append(Tutor.objects.get(user = user_request.tutor_ID_id))

    return render(request = request, template_name = "main/requests_student.html", context={"pending":pending_tutors,"accepted":accepted_tutors})
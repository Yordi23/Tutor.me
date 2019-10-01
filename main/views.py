from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignUp_Form, TutorSignUp_Form, StudentSignUp_Form
from .models import Tutor, User, Subject, Student, User_Request
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

@csrf_exempt
def CreateRequest(request):
    if request.method == "POST":
        tutorId=request.POST.get("Tutor_User","")
        new_student = Student.objects.get(user = request.user.id)
        new_tutor = Tutor.objects.get(user = tutorId)
        user_request = User_Request.objects.create(student_ID=new_student,tutor_ID=new_tutor,)
        user_request.save()
        messages.success(request, f"Solicitud enviada")

    response_data={}
    return JsonResponse(response_data)

@csrf_exempt
def CancelRequest(request):
    if request.method == "POST":
        request_id=request.POST.get("request_id","")
        get_request = User_Request.objects.get(id = request_id)
        get_request.status = 'C'
        get_request.save()
        messages.success(request, f"Solicitud cancelada")

    response_data={}
    return JsonResponse(response_data)


@csrf_exempt
def AcceptRequest(request):
    if request.method == "POST":
        request_id=request.POST.get("request_id","")
        get_request = User_Request.objects.get(id = request_id)
        get_request.status = 'A'
        get_request.save()
        messages.success(request, f"Solicitud aceptada")

    response_data={}
    return JsonResponse(response_data)

@csrf_exempt
def RejectRequest(request):
    if request.method == "POST":
        request_id=request.POST.get("request_id","")
        get_request = User_Request.objects.get(id = request_id)
        get_request.status = 'R'
        get_request.save()
        messages.success(request, f"Solicitud rechazada")

    response_data={}
    return JsonResponse(response_data)


# def homepage(request):
#     return render(request = request, template_name = "main/home.html")

def homepage_tutor(request):
    user_id = None
   
    if request.user.is_authenticated:
        user_id = request.user.id

    user_requests = User_Request.objects.filter(tutor_ID_id=user_id,status='P')
    dic_students = {}
    for user_request in user_requests:
        dic_students[user_request] = Student.objects.get(user = user_request.student_ID_id)

    return render(request = request, template_name = "main/homepage_tutor.html", context={"students":dic_students})

def homepage_student(request):
    # if request.method == "POST":
    #     username=request.POST.get("Tutor_User","")
    #     print(username)
    #     response_data={}
    #     try:
    #         response_data['result']='We got it'
    #         response_data['message']=username
    #     except:
    #         response_data['result']='We cant get it'
    #         response_data['message']='Error'
    #     return JsonResponse(response_data)
    # else:        
    student_requests = User_Request.objects.filter(student_ID = request.user.id, status = 'P')
    tutors = Tutor.objects.all()
    dic_tutors = {}

    for tutor in tutors:
        flag = False
        for student_request in student_requests:
            if tutor.user.id == student_request.tutor_ID_id:
                flag = True
                dic_tutors[tutor] = flag
        
        if flag == False:
            dic_tutors[tutor] = flag

    return render(request = request, template_name = "main/homepage_student.html", context={"tutors":dic_tutors})

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
                    return  redirect("main:homepage_tutor")  #redirect("main:homepage_tutor")
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
    # messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def requests_student(request):
    user_id = None
   
    if request.user.is_authenticated:
        user_id = request.user.id

    pending_user_requests = User_Request.objects.filter(student_ID_id=user_id,status='P')
    accepted_user_requests = User_Request.objects.filter(student_ID_id=user_id,status='A')
    pending_tutors = {}
    accepted_tutors = {}

    for user_request in pending_user_requests:
        pending_tutors[user_request] = Tutor.objects.get(user = user_request.tutor_ID_id)
    
    for user_request in accepted_user_requests:
        accepted_tutors[user_request] = Tutor.objects.get(user = user_request.tutor_ID_id)

    return render(request = request, template_name = "main/requests_student.html", context={"pending":pending_tutors,"accepted":accepted_tutors})

def requests_tutor(request):
    user_id = None
   
    if request.user.is_authenticated:
        user_id = request.user.id

    rejected_user_requests = User_Request.objects.filter(tutor_ID_id=user_id,status='R')
    accepted_user_requests = User_Request.objects.filter(tutor_ID_id=user_id,status='A')
    rejected_students = {}
    accepted_students = {}

    for user_request in rejected_user_requests:
        rejected_students[user_request] = Student.objects.get(user = user_request.student_ID_id)
    
    for user_request in accepted_user_requests:
        accepted_students[user_request] = Student.objects.get(user = user_request.student_ID_id)

    return render(request = request, template_name = "main/requests_tutor.html", context={"rejected":rejected_students,"accepted":accepted_students})
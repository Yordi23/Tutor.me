from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignUp_Form, TutorSignUp_Form
from .models import Tutor,User

# Create your views here.


def homepage(request):
    return render(request = request, template_name = "main/home.html")



def tutor_signup(request):
    # user_form = UserSignUp_Form
    # tutor_form = TutorSignUp_Form

    if request.method == 'POST':
        user_form = UserSignUp_Form(request.POST)        
        tutor_form = TutorSignUp_Form(request.POST)

        if tutor_form.is_valid():
            user = user_form.save()
            
            tutor = Tutor.objects.create(user = user)
            tutor.degree = tutor_form.cleaned_data['degree']
            tutor.identity_document = tutor_form.cleaned_data['identity_document']
            tutor.description = tutor_form.cleaned_data['description']
            tutor.subjects.set = tutor_form.cleaned_data['subjects']
            tutor.save()
            #tutor_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('main:homepage')
        else:
            return HttpResponse("Not valid") #redirect('main:badpage')

    user_form = UserSignUp_Form
    tutor_form = TutorSignUp_Form

    return render (request, "main/tutor_signup.html", context={"user_form":user_form,"tutor_form":tutor_form})
    
    #"user_form":user_form
    #"tutor_form":tutor_form
    
# def homepage(request):
#     return render(request = request, template_name = "main/home.html")

# def StudentSignUpView(request):
#     model = User
#     form_class = StudentSignUpForm
#     template_name = 'registration/signup_form.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('students:quiz_list')
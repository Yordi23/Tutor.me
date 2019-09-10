from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('tutor_signup/', views.tutor_signup, name = "tutor_signup"),
    path('student_signup/', views.student_signup, name = "student_signup"),
]
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('tutor_signup/', views.tutor_signup, name = "tutor_signup"),
    path('student_signup/', views.student_signup, name = "student_signup"),
    path('homepage_tutor/', views.homepage_tutor, name = "homepage_tutor"),
    path('homepage_student/', views.homepage_student, name = "homepage_student"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("requests_student/", views.requests_student, name="requests_student"),
]
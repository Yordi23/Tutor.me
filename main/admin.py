from django.contrib import admin
from .models import Subject, College, Student, Tutor, User_Request, User

# Register your models here.

class SubjectAdmin (admin.ModelAdmin):
    list_display = ('name','area')

class UserAdmin (admin.ModelAdmin):
    list_display = ('id','email',)

class TutorAdmin (admin.ModelAdmin):
    list_display = ('user',)

class UserRequestAdmin (admin.ModelAdmin):
    list_display = ('student_ID','tutor_ID','status')

admin.site.register(User,UserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(College)
admin.site.register(Student)
admin.site.register(Tutor,TutorAdmin)
admin.site.register(User_Request,UserRequestAdmin)
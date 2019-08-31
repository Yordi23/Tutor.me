from django.contrib import admin
from .models import Subject, College, Student, Tutor, User_Request, User

# Register your models here.

class SubjectAdmin (admin.ModelAdmin):
    list_display = ('name','area')


admin.site.register(User)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(College)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(User_Request)
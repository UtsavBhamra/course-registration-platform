from django.contrib import admin
from .models import CustomUser,Student,Faculty,Admin

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Admin)

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Students)
admin.site.register(Admin)
admin.site.register(Lecturers)
admin.site.register(Courses)
admin.site.register(Booked)
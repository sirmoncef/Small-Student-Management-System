from django.contrib import admin
from .models import Student


@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email','phonenumber','Departement')
    search_fields = ('name',)
    list_filter = ('Departement',)



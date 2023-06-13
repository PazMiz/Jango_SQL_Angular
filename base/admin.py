from django.contrib import admin
from .models import Customer
from .models import Books
from .models import School


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'city','age']
    list_display = ['name', 'city', 'age']

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['bookname', 'writer','date']
    list_display = ['bookname', 'writer','date']

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ['Teacher', 'studenets','grade']
    list_display = ['Teacher', 'studenets', 'grade']



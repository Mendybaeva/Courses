from django.contrib import admin
from .models import *


class BranchInline(admin.StackedInline):
    model = Branch
    extra = 1


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [BranchInline, ContactInline, ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Category)

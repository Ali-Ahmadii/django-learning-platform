from django.contrib import admin
from .models import Subject,Course,Module

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Subject,SubjectAdmin)

class ModuleInline(admin.StackedInline):
    model = Module
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
admin.site.register(Course,CourseAdmin)
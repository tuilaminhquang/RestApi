from django.contrib import admin
from .models import User, Category, Course, Lesson
# Register your models here.

admin.AdminSite.site_header = 'Hệ thống quản lý các khóa học trực tuyến'

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'category']
    list_filter = ['category']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['updated_date', 'created_date']



admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)

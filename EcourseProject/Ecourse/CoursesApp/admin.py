from django.contrib import admin
from .models import User, Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

admin.AdminSite.site_header = 'Hệ thống quản lý các khóa học trực tuyến'

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'category']
    list_filter = ['category']
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
                return mark_safe(
                    '<img src="/static/{url}" width="120" />' \
                        .format(url=obj.image.name)
                )

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['updated_date', 'created_date']

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'
class LessonAdmin(admin.ModelAdmin):
    form = LessonForm


admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)

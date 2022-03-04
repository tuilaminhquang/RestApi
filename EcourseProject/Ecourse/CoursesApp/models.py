from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='courses/%Y/%m/')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to='lessons/%Y/%m/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.subject

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



# Generated by Django 4.0.2 on 2022-03-04 12:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0003_tag_alter_lesson_unique_together_lesson_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

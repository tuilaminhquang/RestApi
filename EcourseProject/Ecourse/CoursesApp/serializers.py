from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Course, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    image = SerializerMethodField(source='image')

    def get_image(self, obj):
        request = self.context['request']
        # if obj.image and obj.image.name.startswith("/static"):
        #     pass
        # else:
        path = '/static/%s' % obj.image.name

        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'created_date', 'category', 'image']


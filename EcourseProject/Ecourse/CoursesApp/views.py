from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer

# Create your views here.

class CategoryViewset(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer

    def get_queryset(self):
        q = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            q = q.filter(name__icontains=kw)

        return q


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]





def index(request):
    return HttpResponse('Hello world')

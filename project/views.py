from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializers
from .models import Project

class RequestTestAPI(APIView):

    def get(self, request, format=None):
        return Response({"API": "OK"})

class ProjectCreateViewSet(generics.CreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

class ProjectRetrieveUpdateDeleteViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

class ProjectListViewSet(generics.ListAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
from django.shortcuts import render
from rest_framework import viewsets
from .models import Curso
from .serializer import CursoSerializer
# Create your views here.

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
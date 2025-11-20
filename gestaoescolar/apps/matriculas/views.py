from django.shortcuts import render
from rest_framework import viewsets
from .models import Matricula
from .serializer import MatriculaSerializer

# Create your views here.

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
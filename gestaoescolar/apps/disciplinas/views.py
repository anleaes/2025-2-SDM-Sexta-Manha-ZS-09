from django.shortcuts import render
from rest_framework import viewsets
from .models import Disciplina
from .serializer import DisciplinaSerializer

# Create your views here.


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
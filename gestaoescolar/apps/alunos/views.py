from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno
from .serializer import AlunoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
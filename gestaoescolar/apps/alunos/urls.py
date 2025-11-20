from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'alunos'

router = routers.DefaultRouter()
router.register('', views.AlunoViewSet, basename='alunos')

urlpatterns = [
    path('', include(router.urls)),
]

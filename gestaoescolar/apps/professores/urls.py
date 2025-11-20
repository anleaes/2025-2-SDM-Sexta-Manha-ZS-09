from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'professores'

router = routers.DefaultRouter()
router.register('', views.ProfessorViewSet, basename='professor')

urlpatterns = [
    path('', include(router.urls)),
]

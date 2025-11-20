from django.urls import path, include
from rest_framework import routers
from .views import DisciplinaViewSet

app_name = 'disciplina'

router = routers.DefaultRouter()
router.register('', DisciplinaViewSet, basename='disciplina')

urlpatterns = [
    path('', include(router.urls)),
]

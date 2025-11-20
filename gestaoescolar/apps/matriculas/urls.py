from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'matriculas'

router = routers.DefaultRouter()
router.register('', views.MatriculaViewSet, basename='matriculas')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'turmas'

router = routers.DefaultRouter()
router.register('', views.TurmaViewSet, basename='turmas')

urlpatterns = [
    path('', include(router.urls)),
]

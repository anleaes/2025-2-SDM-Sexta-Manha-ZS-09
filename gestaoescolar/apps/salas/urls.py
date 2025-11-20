from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'salas'

router = routers.DefaultRouter()
router.register('', views.SalaViewSet, basename='salas')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'campus'

router = routers.DefaultRouter()
router.register('', views.CampusViewSet, basename='campus')

urlpatterns = [
    path('', include(router.urls)),
]

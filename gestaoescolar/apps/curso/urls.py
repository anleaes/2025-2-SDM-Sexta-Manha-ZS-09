from django.urls import path, include
from rest_framework import routers
from .views import CursoViewSet

app_name = 'curso'

router = routers.DefaultRouter()
router.register('', CursoViewSet, basename='curso')

urlpatterns = [
    path('', include(router.urls)),
]
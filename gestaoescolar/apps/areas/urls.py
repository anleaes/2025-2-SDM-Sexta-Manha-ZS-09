from django.urls import path, include
from rest_framework import routers
from .views import AreaViewSet

app_name = 'area'

router = routers.DefaultRouter()
router.register('', AreaViewSet, basename='area')

urlpatterns = [
    path('', include(router.urls)),
]

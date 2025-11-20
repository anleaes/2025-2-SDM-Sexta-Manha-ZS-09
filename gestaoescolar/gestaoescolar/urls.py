"""
URL configuration for gestaoescolar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('areas/', include('areas.urls', namespace='areas')),
    path('curso/', include('curso.urls', namespace='curso')),
    path('disciplina/', include('disciplinas.urls', namespace='disciplinas')),
    path('professores/', include('professores.urls', namespace='professores')),
    path('campus/', include('campus.urls', namespace='campus')),
    path('salas/', include('salas.urls', namespace='salas')),
    path('turmas/', include('turmas.urls', namespace='turmas')),
    path('alunos/', include('alunos.urls', namespace='alunos')),
    path('matriculas/', include('matriculas.urls', namespace='matriculas')),


]


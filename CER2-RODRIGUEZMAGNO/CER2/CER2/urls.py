# urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.onePage, name='onePage'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('nuevo-proyecto/', views.nuevo_proyecto, name='nuevo_proyecto'),
    path('modificar-proyecto/<int:proyecto_id>/', views.modificar_proyecto, name='modificar_proyecto'),
    path('patrocinar-proyecto/<int:proyecto_id>/', views.patrocinar_proyecto, name='patrocinar_proyecto'),
    path('login/', auth_views.LoginView.as_view(template_name='core/onePage.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

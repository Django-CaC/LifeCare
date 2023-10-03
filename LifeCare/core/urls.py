from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('login/',views.login, name='login'),
    path('usuario/<str:usuario_activo>',views.usuario_registrado, name='usuario_registrado'),
    path('contacto/', views.contacto, name='contacto'),
]
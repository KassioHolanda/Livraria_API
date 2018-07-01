from django.urls import path

# from django.conf.urls import url, include

from user import views

urlpatterns = [
    path('user/', views.UsuarioList.as_view(), name=views.UsuarioList.name),
    path('user/<int:pk>', views.UsuarioDetail.as_view(), name=views.UsuarioDetail.name),
]

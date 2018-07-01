
from user import views
from django.urls import include, path

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('user/', views.UsuarioList.as_view(), name=views.UsuarioList.name),
    path('user/<int:pk>', views.UsuarioDetail.as_view(), name=views.UsuarioDetail.name),
]

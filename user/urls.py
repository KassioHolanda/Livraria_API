
from user import views
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Users')

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('user/', views.UsuarioList.as_view(), name=views.UsuarioList.name),
    path('user/<int:pk>', views.UsuarioDetail.as_view(), name=views.UsuarioDetail.name),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

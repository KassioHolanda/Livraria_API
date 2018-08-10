
from user import views
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_swagger_view(title='Users')

urlpatterns = [
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.UsuarioList.as_view(), name=views.UsuarioList.name),
    path('user/<int:pk>', views.UsuarioDetail.as_view(), name=views.UsuarioDetail.name),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

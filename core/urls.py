from django.urls import path
from core import views
from rest_framework.routers import DefaultRouter


from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Livraria API')

router = DefaultRouter()
router.register('titulo', views.TituloViewSet, base_name=views.TituloViewSet.name)
router.register('autor', views.AutorViewSet, base_name=views.AutorViewSet.name)
router.register('categoria', views.CategoriaViewSet, base_name=views.CategoriaViewSet.name)
router.register('editora', views.EditoraViewSet, base_name=views.EditoraViewSet.name)


urlpatterns = router.urls


    #path('docs/', schema_view)
   # path('titulo/', views.TituloViewSet.as_view({'get':'list', 'post': 'create'}), name=views.TituloViewSet.name),
   # path('autor/', views.AutorViewSet.as_view({'get':'list', 'post': 'create'}), name=views.AutorViewSet.name),
   # path('categoria/', views.CategoriaViewSet.as_view({'get':'list', 'post': 'create'}), name=views.CategoriaViewSet.name),
   # path('editora/', views.EditoraViewSet.as_view({'get':'list', 'post': 'create'}), name=views.EditoraViewSet.name),

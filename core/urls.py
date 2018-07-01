from django.urls import path
from core import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

    path('titulo/', views.TituloList.as_view(), name=views.TituloList.name),
    path('titulo/<int:pk>', views.TituloDetail.as_view(), name=views.TituloDetail.name),

    path('livro/', views.LivroList.as_view(), name=views.LivroList.name),
    path('livro/<int:pk>', views.LivroDetail.as_view(), name=views.LivroDetail.name),

    path('emprestimo/', views.EmprestimoList.as_view(), name=views.EmprestimoList.name),
    path('emprestimo/<int:pk>', views.EmprestimoDetail.as_view(), name=views.EmprestimoDetail.name),
]

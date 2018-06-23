from django.urls import path

# from django.conf.urls import url, include

from user import views

urlpatterns = [
    path('user/', views.UserList.as_view(), name=views.UserList.name),
    path('user/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
]

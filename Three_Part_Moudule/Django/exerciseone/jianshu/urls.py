
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('write/', views.write_article, name='write'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register')
]
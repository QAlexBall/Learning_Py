
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('write/', views.write_article, name='write'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('write_comment/<int:article_id>/', views.write_comment, name='write_comment'),
    path('<int:article_id>/', views.article_content, name='article_content'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<int:id>/', views.news_detail, name='news-detail'),
    path('news/', views.news, name='news'),
]
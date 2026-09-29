from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('carta/<int:card_id>/', views.card_detail, name='card_detail'),
]
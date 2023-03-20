from django.urls import path
from . import views

urlpatterns = [
    path('', views.tubs_view, name='tubs'),
    path('stores/', views.stores_view, name='stores'),
    path('stores/<int:id>/', views.store_view, name='store'),
]

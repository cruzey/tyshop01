from django.urls import path
from . import views


app_name = 'tyadmins'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('prodinfo/<int:product_pk>/', views.prodinfo_view, name='prodinfo'),
]
from django.urls import path

from .import views

app_name = 'item'

urlpatterns = [
    path('new/',views.new,name='new'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/delete_confirmation/', views.delete_confirmation, name='delete_confirmation'),
    path('cancel_delete/', views.cancel_delete, name='cancel_delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),
] 

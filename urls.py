from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name = 'std_form'),
    path('show', views.show, name = 'std_show'),
    path('<int:id>/', views.add, name = 'std_update'),
    path('delete/<int:id>/', views.delete, name = 'std_delete'),
    path('showProject', views.show, name = 'std_show')
    ]
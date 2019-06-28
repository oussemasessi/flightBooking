from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^Airplane_list/', views.Airplane_list, name = 'list'),
    path(r'^Airplane_update/(\d+)/$', views.Airplane_update, name='update'),
    path(r'^Airplane_delete/(\d+)/$', views.Airplane_delete, name = 'delete'),
    path(r'^Airplane_create/$', views.Airplane_create, name = 'create'),
]
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('delete/ta/<str:pk>', views.delete_ta, name='delete'),
	path('delete/th/<str:pk>', views.delete_th, name='delete'),
	path('delete/ha/<str:pk>', views.delete_ha, name='delete')
]
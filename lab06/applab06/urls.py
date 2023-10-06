from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='detalles_producto'),  # Cambiar a 'producto'
    path('producto/', views.producto, name='nuevo_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]

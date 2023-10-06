from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.producto, name='detalles_producto'),  # Cambiar a 'producto'
    path('producto/', views.producto, name='nuevo_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]

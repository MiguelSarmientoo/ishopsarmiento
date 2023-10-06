from django.db import models
from django.db.models.fields.files import ImageField

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pub_date = models.DateTimeField('fecha de registro', auto_now=True)

    def __str__(self):
        return self.nombre

from django.db import models
from django.db.models.fields.files import ImageField

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    image = ImageField(upload_to='media/images/')

    def __str__(self):
        return self.nombre
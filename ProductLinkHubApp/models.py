from django.db import models

# Create your models here.

class Categorias(models.Model):
    categoria = models.CharField(max_length=200)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.categoria}"

    class Meta():
        verbose_name = "Categorias"
        verbose_name_plural = "Categorias"


class SubCategorias(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.nombre}"
    

    class Meta():
        verbose_name = "SubCategorias"
        verbose_name_plural = "SubCategorias"


class Product(models.Model):
    product = models.TextField()
    subcategoria = models.ManyToManyField(SubCategorias)
    disponible = models.BooleanField(default=True)

    def subcategorias(self):
        subcategorias = self.subcategoria.all()
        lista_subcategorias_totales = []

        for subcategoria in subcategorias:
            lista_subcategorias_totales.append(subcategoria)
        return lista_subcategorias_totales 


    class Meta():
        verbose_name = "Product"
        verbose_name_plural = "Products"

class ImagenFondo(models.Model):
    imagen = models.ImageField(upload_to="ProductLinkHubApp/media/imagenes_fondo")
    enlace = models.URLField(blank=True, null=True)
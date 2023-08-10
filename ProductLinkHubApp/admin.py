from django.contrib import admin
from .models import *

# Register your models here.

class AdminCategorias(admin.ModelAdmin):
    list_display = ['categoria', 'disponible']

class AdminSubCategorias(admin.ModelAdmin):
    list_display = ['nombre', 'get_categoria', 'disponible']

    def get_categoria(self, obj):
        return obj.categoria.categoria

    get_categoria.short_description = 'Categoría'

class AdminProduct(admin.ModelAdmin):
    list_display = ['product', 'subcategorias', 'disponible']

class AdminImagenFondo(admin.ModelAdmin):
    list_display = ['enlace', 'imagen']
    list_display_links = ['enlace']

class AdminSubCategoriaSeccion(admin.ModelAdmin):
    list_display = ['nombre', ]

class AdminProductSubCategoriaSeccion(admin.ModelAdmin):
    list_display = ['product', 'subcategorias_seccion', 'disponible']


admin.site.register(Categorias, AdminCategorias)
admin.site.register(SubCategorias, AdminSubCategorias)
admin.site.register(Product, AdminProduct)
admin.site.register(ImagenFondo, AdminImagenFondo)
admin.site.register(SubCategoriaSeccion, AdminSubCategoriaSeccion)
admin.site.register(ProductSubCategoriaSeccion, AdminProductSubCategoriaSeccion)



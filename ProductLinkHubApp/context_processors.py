from .models import Categorias, SubCategoriaSeccion

def categorias(request):
    categorias = Categorias.objects.all()
    return {'categorias': categorias}

def subcategoriaseccion(request):
    subcategoriaseccion = SubCategoriaSeccion.objects.all()
    return {'subcategoriaseccion': subcategoriaseccion}



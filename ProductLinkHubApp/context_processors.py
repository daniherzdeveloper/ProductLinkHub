from .models import Categorias, ImagenFondo

def categorias(request):
    categorias = Categorias.objects.all()
    return {'categorias': categorias}

def imagenfondo(request):
    imagenes = ImagenFondo.objects.all()
    url_imagenes = []
    
    for imagen in imagenes:
        url_imagenes.append({"imagen": imagen.imagen.url, "enlace": imagen.enlace})
     
    return {'url_imagenes': url_imagenes}

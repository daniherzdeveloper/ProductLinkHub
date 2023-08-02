from .models import Categorias

def categorias(request):
    categorias = Categorias.objects.all()
    return {'categorias': categorias}



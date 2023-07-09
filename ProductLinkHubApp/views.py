from django.views.generic import TemplateView
from .models import SubCategorias, ImagenFondo
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator

# Create your views here.

class MejorRelacionCalidadPrecio(TemplateView):
    template_name = "ProductLinkHubApp/mejor_relacion_calidad_precio.html"
    paginate_by = 16  # Número de elementos por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        subcategoria = SubCategorias.objects.get(pk=7)
        productos = subcategoria.product_set.filter(disponible=True)
        imagenes = ImagenFondo.objects.all()
        
        paginator = Paginator(productos, self.paginate_by)  # Objeto Paginator
        
        page_number = self.request.GET.get('page')  # Obtener el número de página actual

        # Obtener la página actual
        page_obj = paginator.get_page(page_number)

        for producto in page_obj:
            producto.product = mark_safe(producto.product)

        

        context['productos'] = page_obj
        context['subcategoria'] = subcategoria
        context['imagenes'] = imagenes

        return context


class MasVendidosGenerales(TemplateView):
    template_name = "ProductLinkHubApp/template_products.html"
    paginate_by = 16  # Número de elementos por página


    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)

        subcategoria = SubCategorias.objects.get(pk=pk)
        productos = subcategoria.product_set.filter(disponible=True)
        categoria = subcategoria.categoria
        
        paginator = Paginator(productos, self.paginate_by)  # Objeto Paginator
        
        page_number = self.request.GET.get('page')  # Obtener el número de página actual

        # Obtener la página actual
        page_obj = paginator.get_page(page_number)

        for producto in page_obj:
            producto.product = mark_safe(producto.product)

        context['productos'] = page_obj
        context['categoria'] = categoria

        return context

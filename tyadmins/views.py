from django.shortcuts import render
from .models import Product

# Create your views here.
def list(request):
    get_product = Product.objects
    query = request.GET.get('query','')
    if query:
        get_product = get_product.filter(name__icontains=query)
    context = {
       'get_product' : get_product
    }
    return render(request, 'list.html', context)

def prodinfo_view(request, product_pk):
    prod = Product.objects.get(pk=product_pk)
    context = {
            'prod': prod
        }
    return render(request, 'prodinfo.html', context)
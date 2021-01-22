from django.shortcuts import render, redirect
from tyadmins.models import Product
# Create your views here.

def index(request):
    get_products = Product.objects.all()[ :4]
    # query = request.GET.get('query','')
    # if query:
    #     get_product = get_product.filter(name__icontains=query)
    context = {
       'get_products' : get_products
    }
    return render(request, 'tyhome/index.html', context)

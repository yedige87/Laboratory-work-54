from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse

from shop_app.models import Product, Category


def products_view(request: WSGIRequest):
    return redirect('index')


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={'product': product})


def categories_view(request: WSGIRequest):
    pass


def category_add_view(request: WSGIRequest):
    pass


def product_add_view(request: WSGIRequest):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'product_add.html', context={'categories': categories})
    print(request.POST)
    prod_data = {
        'title': request.POST.get('title'),
        'price': request.POST.get('price'),
        'photo': request.POST.get('photo'),
        'cat_id': request.POST.get('cat_id'),
        'description': request.POST.get('description'),
    }
    if prod_data['photo'] == '':
        prod_data['photo'] = 'blank.jpg'

    product = Product.objects.create(**prod_data)
    return redirect(reverse('product_view', kwargs={'pk': product.pk}))


def category_edit_view(request: WSGIRequest):
    pass


def product_edit_view(request: WSGIRequest):
    pass

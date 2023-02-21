from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, get_object_or_404, render

from shop_app.models import Product


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
    pass


def category_edit_view(request: WSGIRequest):
    pass


def product_edit_view(request: WSGIRequest):
    pass

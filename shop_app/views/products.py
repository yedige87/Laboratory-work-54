from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from shop_app.models import Product, Category


def products_view(request: WSGIRequest):
    return redirect('index')


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={'product': product})


def category_add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'category_add.html')
    print(request.POST)
    cat_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
    }
    # category = Category.objects.create(**cat_data)
    Category.objects.create(**cat_data)
    return redirect('index') #, kwargs={'pk': category.pk}))


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


def categories_view(request: WSGIRequest):
    categories = Category.objects.all()
    return render(request, 'categories_view.html', context={'categories': categories})


def category_delete_view(request: WSGIRequest,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('index')


def category_edit_view(request: WSGIRequest, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        return render(request, 'category_edit.html',context={'category': category})
    print(request.POST)
    category.title = request.POST.get('title'),
    category.description = request.POST.get('description'),
    category.save()
    return redirect('categories_view')


def product_delete_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')


def product_edit_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'product_edit.html', context={'product': product, 'categories': categories})
    print(request.POST)
    product.title = request.POST.get('title'),
    product.price = request.POST.get('price'),
    product.photo = request.POST.get('photo'),
    product.cat_id = request.POST.get('cat_id'),
    product.description = request.POST.get('description'),
    if product.photo == '':
        product.photo = 'blank.jpg'
    product.save()
    return redirect(reverse('product_view', kwargs={'pk': product.pk}))

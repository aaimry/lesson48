from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

from store.forms import ProductsForm
from store.models import Products


def product_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        product = Products.objects.filter(title__icontains=search_query).order_by('title', 'category')
    else:
        product = Products.objects.all().order_by('title', 'category')
    return render(request, 'products.html', {'product': product})


def product_add_view(request):
    if request.method == 'GET':
        form = ProductsForm()
        return render(request, 'products_add.html', {'form': form})
    else:
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            if description == '':
                description = 'Отсутстувет'
            category = form.cleaned_data.get('category')
            residue = form.cleaned_data.get('residue')
            price = form.cleaned_data.get('price')
            new_product = Products.objects.create(title=title, description=description, category=category,
                                                  residue=residue, price=price)
            return redirect('product_check', pk=new_product.pk)
        return render(request, 'products_add.html', {'form': form})


def product_check_view(request, pk):
    try:
        check_product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return HttpResponseNotFound('Продукт не найден')
    context = {'products_list': check_product}
    return render(request, 'product_check.html', context)


def update_product_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        form = ProductsForm(initial={
            'title': product.title,
            'description': product.description,
            'category': product.category,
            'residue': product.residue,
            'price': product.price
        })
        return render(request, 'update_product.html', {'product': product, 'form': form})
    else:
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            product.title = form.cleaned_data.get('title')
            product.description = form.cleaned_data.get('description')
            if product.description == '':
                product.description = 'Отсутстувет'
            product.category = form.cleaned_data.get('category')
            product.residue = form.cleaned_data.get('residue')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect('product_check', pk=product.pk)
        return render(request, 'update_product.html', {'product': product, 'form': form})


def product_delete_view(request, pk):
    product = Products.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', {'product': product})
    else:
        product.delete()
        return redirect('index')


def product_category_view(request, category):
    category = Products.objects.filter(category=category).order_by('title')
    if request.method == 'POST':
        if category:
            category = Products.objects.filter(category__icontains=category)
    return render(request, 'product_category.html', {'product': category})

from django.shortcuts import render, redirect
from .models import Products
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def add_product(request):
    if request.method == "POST":
        prod_name = request.POST.get("p-name")
        prod_quantity = request.POST.get("p-qtty")
        prod_size = request.POST.get("p-size")
        prod_price = request.POST.get("p-price")
        context = {
            "prod_name": prod_name,
            "prod_quantity": prod_quantity,
            "prod_size": prod_size,
            "prod_price": prod_price,
            "success": "Data saved successfully"
        }
        query = Products(name=prod_name, qtty=prod_quantity,
                         size=prod_size, price=prod_price)
        query.save()

        return render(request, 'add-product.html', context)
    return render(request, 'add-product.html')


def products(request):
    all_products = Products.objects.all()
    context = {"all_products": all_products}
    return render(request, 'products.html', context)

def delete_product(request, id):
    product =Products.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('all-products')

def update_product(request, id):
    product = Products.objects.get(id=id)
    context = {"product": product}
    if request.method == "POST":
        updated_name = request.POST.get('p-name')
        updated_qtty = request.POST.get('p-qtty')
        updated_size = request.POST.get('p-size')
        updated_price = request.POST.get('p-price')
        product.name = updated_name
        product.qtty = updated_qtty
        product.size = updated_size
        product.price = updated_price
        product.save()
        messages.success(request, 'Product updated successfully')
        return redirect('all-products')
    return render(request, 'update-product.html', context)
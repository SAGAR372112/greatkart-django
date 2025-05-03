from django.shortcuts import render
<<<<<<< HEAD
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')

    # Get the reviews

    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
=======
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
>>>>>>> 6279ca3506e3df2c5e607c86e0ec763a2aeae867
    }

    return render( request, 'home.html', context)


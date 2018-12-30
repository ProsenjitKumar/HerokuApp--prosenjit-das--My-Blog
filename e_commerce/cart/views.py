from django.shortcuts import render


def cart(request):
    return render(request, 'e_commerce/cart/cart.html')

from django.shortcuts import render


def reviews(request):
    return render(request, 'subscription_join/ajax.html')


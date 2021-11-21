from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Index',
        'products': [
            {'name': 'stool', 'price': 2585.1},
            {'name': 'stool2', 'price': 11124.9},
            {'name': 'stool3', 'price': 35367.5},
            {'name': 'stool4', 'price': 56664.4},
            {'name': 'stool5', 'price': 36463.8},

        ],

    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'products',
        'products': [
            {'name': 'stool', 'price': 2585.1},
            {'name': 'stool2', 'price': 11124.9},
            {'name': 'stool3', 'price': 35367.5},
            {'name': 'stool4', 'price': 56664.4},
            {'name': 'stool5', 'price': 36463.8},

        ],

    }
    return render(request, 'mainapp/products.html', context)


def contact(request):

    return render(request, 'mainapp/contact.html')




from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Index',
        'header': '',

    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'products',
        'header': '',

    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'contact',
        'header': '',

    }
    return render(request, 'mainapp/contact.html', context)




from django.shortcuts import render
from . import models


def index(request, city):
    city = models.City.objects.get(pk=city)
    business_list = models.Business.objects.filter(neighborhood__city=city)
    category = None
    neighborhood = None

    if request.GET.get('c'):
        try:
            category = models.Category.objects.get(pk=request.GET.get('c'))
            business_list = business_list.filter(category=category)
        except:
            pass

    if request.GET.get('n'):
        try:
            neighborhood = city.neighborhood_set.get(pk=request.GET.get('n'))
            business_list = business_list.filter(neighborhood=neighborhood)
        except:
            pass

    context = {
        'city': city,
        'business_list': business_list,
        'category': category,
        'neighborhood': neighborhood,
        'category_list': models.Category.objects.all().order_by('title')
    }
    return render(request, 'directory/index.html', context)
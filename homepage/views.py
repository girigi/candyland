from django.shortcuts import render
from candy.models import Candies
from django.db.models import Q

# Create your views here.


def index(request):
    template = 'homepage/index.html'
    query = request.GET.get('q')
    candy_list = Candies.objects.filter(is_published=True)
    if query:
        candy_list = candy_list.filter(
            Q(title__icontains = query) |
            Q(description__icontains = query)
        )
    else:
        candy_list = candy_list.filter(is_on_main=True)

    context = {
        'candy_list': candy_list,
        'query': query
    }
    return render(request, template, context)

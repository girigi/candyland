from django.shortcuts import render
from candy.models import Candies
from django.db.models import Q

# Create your views here.


def index(request):
    template = 'homepage/index.html'
    candy_list = Candies.objects.values(
        'id', 'title', 'description'
        ).filter(is_on_main=True, is_published=True)
    context = {'candy_list': candy_list}
    return render(request, template, context)

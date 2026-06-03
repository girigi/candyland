from django.shortcuts import render
from candy.models import Candies

# Create your views here.
def bascet_list(request):
    template = 'bascet/list.html'
    context = {
        'cart_items': [
            {'id': 1, 'name': 'Мороженое "Сказка"', 'price': 250, 'quantity': 2, 
             'total': 500, 'image': '/static/img/ice1.jpg', 'description': 'Ванильное с шоколадом'},
            # ... остальные товары из сессии или БД
        ],
        'total_amount': 1250,
        'discount': 10,
        'discount_amount': 125,
        'final_amount': 1125,
        'recommendations': Candies.objects.exclude(id__in=cart_ids)[:4],
        'popular_products': Candies.objects.filter(is_popular=True)[:4],
    }
    return render(request, template, context)
    
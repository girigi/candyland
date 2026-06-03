from django.shortcuts import get_object_or_404, render
from candy.models import Candies
# Create your views here.



def candy_list(request):
    template = 'candy/list.html'
    query = request.GET.get('q')

    candy_list = Candies.objects.filter(
        is_published=True
        ).only(
            'id',
            'title',
            'description')
    if query:
        candy_list = Candies.objects.filter(title__contains=query, is_published=True)
    context = {'candy_list': candy_list}
    return render(request, template, context)


def candy_detail(request, pk):
    template = 'candy/detail.html'
    candy_detail = get_object_or_404(Candies, pk=pk, is_published=True)
    context = {'candy_detail': candy_detail}
    return render(request, template, context)

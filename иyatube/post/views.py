from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse('Постики')

# Create your views here.

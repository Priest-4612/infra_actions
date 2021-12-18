from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!', status_code=200)


def second_page(request):
    return HttpResponse('А это вторая страница', status_code=200)

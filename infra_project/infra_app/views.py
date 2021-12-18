from http import HTTPStatus

from django.http import HttpResponse


def index(request):
    res = HttpResponse()
    res.content = 'У меня получилось!'
    res.status_code = HTTPStatus.OK
    return res


def second_page(request):
    res = HttpResponse()
    res.content = 'А это вторая страница'
    res.status_code = HTTPStatus.OK
    return res

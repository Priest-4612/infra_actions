from http import HTTPStatus

from django.http import HttpResponse


def index(request):
    res = HttpResponse()
    res.status_code = HTTPStatus.OK
    res.content = 'У меня получилось!'
    return res


def second_page(request):
    res = HttpResponse()
    res.status_code = HTTPStatus.OK
    res.content = 'А это вторая страница!'
    return res

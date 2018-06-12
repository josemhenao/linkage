from django.http import HttpResponse


def registrar(request):
    return HttpResponse("Hello, world. This is the register page.")
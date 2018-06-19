from django.shortcuts import render


def registrar(request):
    return render(request,'register.html')
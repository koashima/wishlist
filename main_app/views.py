from django.shortcuts import render


def wish_list(request):
    return render(request, 'index.html')
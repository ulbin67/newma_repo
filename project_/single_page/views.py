from django.shortcuts import render

# Create your views here.

def maincall(request):
    return render(
        request,
        'single_page/main.html'
    )

def introcall(request):
    return render(
        request,
        'single_page/introduce.html'
    )

def infocall(request):
    return render(
        request,
        'single_page/information.html'
    )
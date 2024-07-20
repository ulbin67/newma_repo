from django.shortcuts import render

# Create your views here.

def applycall(request):
    return render(
        request,
        'manage_apply/apply_page.html'
    )
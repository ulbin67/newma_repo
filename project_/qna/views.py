from django.shortcuts import render
from .models import FAQ

# Create your views here.

from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_list.html', {'faqs': faqs})


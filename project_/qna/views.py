from django.shortcuts import render, get_object_or_404
from .models import FAQ

# Create your views here.


from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_list.html', {'faqs': faqs})

def faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    return render(request, 'faq_detail.html', {'faq':faq})
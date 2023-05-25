from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

def terms(request):
    return render(request, 'terms.html')

def about(request):
    return render(request, 'about.html')

def abuse(request):
    return render(request, 'abuse.html')

def contact(request):
    return render(request, 'contact.html')

def vpsserver(request):
    return render(request, 'vps.html')

def hosting(request):
    return render(request, 'hosting.html')

def domains(request):
    return render(request, 'domains.html')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
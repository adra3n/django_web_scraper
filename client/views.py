from django.shortcuts import render
from .forms import ScrapeForm
import requests
from bs4 import BeautifulSoup

def scrape(request):
    if request.method == 'POST':
        form = ScrapeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            element_type = form.cleaned_data['element_type']
            element_name = form.cleaned_data['element_name']

            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            if element_type == 'id':
                element = soup.find(id=element_name)
            else:
                element = soup.find(class_=element_name)

            return render(request, 'result.html', {'element': element})
    else:
        form = ScrapeForm()

    return render(request, 'form.html', {'form': form})

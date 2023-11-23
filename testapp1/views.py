from django.shortcuts import render
import requests
import random
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html')

def api_data(request):
    api_url = "https://fakestoreapi.com/products"  # Replace with the actual API URL
    response = requests.get(api_url)



    if response.status_code == 200:
        data = response.json()
        return render(request, 'api.html', {'data': data})
    else:
        error_message = "Failed to fetch data from the API."
        return render(request, 'error.html', {'error_message': error_message})


def get_photo(product_id):
    api_url = f'https://fakaestoreapi/products'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_url = response.json().get('photo_url')
        return photo_url
    else:
        return None
from django.shortcuts import render
import requests
from .models import *
# Create your views here.
def index(request):
    # listings = Listings.objects.all()
    # context = {
    #     'listings' : listings,
    # }
    data = {}
    data["crypto_data"] = get_crypto_data()
    return render(request, 'blog/index.html', data)
# return the data received from api as json object
def get_crypto_data():
    api_url = "https://api.coindesk.com/v1/bpi/currentprice/IRR.json"

    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = dict()

    return data
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
import geocoder
import pandas as pd
from django.core.serializers import serialize
from .models import Search, Store
from .forms import SearchForm
from flask import request
import csv
import json


# Create your views here.
def index(request):
    stores = pd.read_csv("ThriftStores.csv")
    data = []
    for index, store in stores.iterrows():
        store = {

            "lat": store['LAT'],
            "long": store['LONG'],
            "popup": f"{store['CITY']},{store['STORE_NAME']},{store['ADDRESS']},{store['OPEN_TIME']},{store['PHONE_NR']}"

        }
        data.append(store)


    return JsonResponse(data, safe=False)


def page(request):
    return render(request, 'index.html')



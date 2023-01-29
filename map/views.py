from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

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



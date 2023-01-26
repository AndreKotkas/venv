from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
import geocoder
import pandas as pd
from .models import Search
from .forms import SearchForm
import csv


# Create your views here.
def index(request) :
    if request.method == 'POST' :
        form = SearchForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/')

    else :
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    long = location.lng
    country = location.country
    if lat == None or long == None :
        address.delete()
        return HttpResponse('Address you input is invalid')
    # Create map object

    franchies = pd.read_csv("ThriftStores.csv")


    for index, franchies in franchies.iterrows():
        location = {

                  "lat" : franchies['LAT'],
                  "long" : franchies['LONG'],
                  "city" : franchies["CITY"],
                  "Sname" : franchies["STORE_NAME"],
                  "addr" : franchies["ADDRESS"],
                  "Otime" : franchies["OPEN_TIME"],
                  "NR": franchies["PHONE_NR"]

                 }
        return JsonResponse(location, safe=False)
        # location = [franchies['LAT'], franchies['LONG']]
        # folium.Marker(location, popup=f'{franchies["CITY"], franchies["STORE_NAME"], franchies["ADDRESS"], franchies["OPEN_TIME"], franchies["PHONE_NR"]}').add_to(m)


    # #Get HTML Representation of Map Objects
    return render(request, 'index.html')

# franchies = pd.read_csv("ThriftStores.csv")
# franchies.head()

# location = [
#     {
#         lat: [franchies['LAT'],
#         long: [franchies['LONG'],
#         popup: '<p>franchies["CITY"]</p><br><p>franchies["STORE_NAME"]</p><br><p>franchies["ADDRESS"]</p><br><p>franchies["OPEN_TIME"]</p><br><p>franchies["PHONE_NR"]</p>'
#
#     }
# ];
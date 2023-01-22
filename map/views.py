from django.shortcuts import render, redirect
from django.http import HttpResponse
import folium
import geocoder
import branca
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
    lng = location.lng
    country = location.country
    if lat == None or lng == None :
        address.delete()
        return HttpResponse('Address you input is invalid')
    # Create map object

    franchies = pd.read_csv("ThriftStores.csv")
    franchies.head()
    m = folium.Map(location=[59, 25], zoom_start=8)
    for index, franchies in franchies.iterrows():
        location = [franchies['LAT'], franchies['LONG']]
        folium.Marker(location, popup=f'{franchies["CITY"], franchies["STORE_NAME"], franchies["ADDRESS"], franchies["OPEN_TIME"], franchies["PHONE_NR"]}').add_to(m)


    # #Get HTML Representation of Map Objects
    m = m._repr_html_()
    context = {
        'm' : m,
        'form' : form,
    }
    return render(request, 'index.html', context)

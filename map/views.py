from django.shortcuts import render, redirect
from django.http import HttpResponse
import folium
import geocoder
from .models import Search
from .forms import SearchForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Address you inbut is unvalid')
    #Create map object
    m = folium.Map(location=[59, 25], zoom_start=8)
    #folium.Marker([58.378485, 26.730052], tooltip='Click for more', popup='Sõbralt Sõbrale').add_to(m)

    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    #Get HTML Representation of Map Objects
    m = m._repr_html_()
    context ={
        'm': m,
        'form': form,
    }
    return render(request, 'index.html', context)
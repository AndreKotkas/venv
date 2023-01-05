from django.shortcuts import render
import folium

# Create your views here.
def index(request):
    #Create map object
    m = folium.Map(location=[59, 25], zoom_start=8)
    folium.Marker([58.378485, 26.730052], tooltip='Click for more', popup='Sõbralt Sõbrale').add_to(m)
    #Get HTML Representation of Map Objects
    m = m._repr_html_()
    context ={
        'm': m,
    }
    return render(request, 'index.html', context)
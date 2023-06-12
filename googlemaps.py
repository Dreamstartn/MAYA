
from msilib.schema import Feature
#from turtle import delay
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web
from Body.Speak import Speak



def GoogleMaps(Place):
    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place, addressdetails = True)
    
    target_location = location.latitude , location.longitude

    location = location.raw['address']

    target = {'city': location.get('city', ''),
                'state' : location.get('state', ''),
                'country' : location.get('country', '') }

    your=str(input("Enter your current loaction: "))
    current_loca = geolocator.geocode(your, addressdetails = True)
    current_location = current_loca.latitude , current_loca.longitude
     
    current_loca = current_loca.raw['address']
    
   
    distance = str(great_circle(current_location, target_location))
    distance = str(distance.split(' ',1)[0]) 
    distance = round(float(distance),2)           

    web.open (url=Url_Place)

    Speak (target)
    #delay(5.8)
    Speak (f" sir, {Place} is {distance} kilometer Away From Your Location.")


GoogleMaps("Rohtak")

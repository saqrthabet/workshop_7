
from .controllers.hotel import *
from .controllers.customer import *
from .controllers.reservation import *
from .controllers.notification import *
from .controllers.main import *
from .controllers.tester import *

from django.http import HttpResponse

def InitializeData(request):
    return HttpResponse("Welcome to My program Hotels_Reservation")

def HotelList(request):
    hotel_list_output = "<ul>"
    for h in Hotel.hotels:
        hotel_list_output += "<li>" + h.hotel_name + "</li>"
    hotel_list_output += "</ul>"
    return HttpResponse(hotel_list_output)

def HotelInCity(request):
    # call the functions to fill all the data about hotels, customers, and reservations
    # select any city = Aden
    hotel_in_city_output = "<ul>"
    for place in Hotel.hotels:
        if "Aden" == place.city:             #hotel_name,empty_rooms
            hotel_in_city_output += "<li>" + place.hotel_name +", Number of empty rooms:" +str(place.empty_rooms) + "</li>"
    hotel_in_city_output += "</ul>"
    return HttpResponse(hotel_in_city_output)
def ReservationList(request):
    # call the functions to fill all the data about hotels, customers, and reservations
    # select any hotel= Holydayin
    reservation_list_output = "<ul>"
    for hoTel in Reservation.reservations:
        if "Holydayin" == hoTel.hotel_name: #hotel_name,customer,.number
            reservation_list_output += "<li>" + " Reservations at " + hoTel.hotel_name + " customer name:" + hoTel.customer +"- Number:"+ hoTel.number + "</li>"
    reservation_list_output += "</ul>"
    return HttpResponse(reservation_list_output)
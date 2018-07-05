
"""
tester.py
This is the tester class file 
"""

from .hotel import *    # will include all classes & functions at that python file
#from .hotel import Hotel  # when you import you will use file name not class name
#import hotel # will include only the functions in <hotel.py>
from .customer import Customer
from .reservation import *   # will include all classes & functions at that python file
#from .reservation import Reservation # will include only the class<Reservation>
#import reservation # will include only the functions in <reservation.py>
from .notification import Notifications
 

class Tester: 
    def fill_test(self): 
        show=Notifications() 
        Rotana_hotel = Hotel(1,"Rotana","Abu Dhabi",200,40)
        Rotana_hotel.add_hotel()
        show.display(Rotana_hotel)  # Display General details for ONE hotels
        Sheraton_hotel = Hotel(2,"Sheraton","Abu Dhabi",300,100)
        Sheraton_hotel.add_hotel()
        Hayat_hotel = Hotel(3,"Hayat","Aden",150,100)
        Hayat_hotel.add_hotel()
        Crecent_hotel = Hotel(4,"Crecent","Mukala",200,50)
        Crecent_hotel.add_hotel()
        Holydayin_hotel = Hotel(5,"Holydayin","Sana'a",200,100)
        Holydayin_hotel.add_hotel()
        Crowne_hotel = Hotel(6,"Crowne","Aden",180,40)
        Crowne_hotel.add_hotel()
        Zero_hotel = Hotel(7,"Zero","Virtual",200,0)  # used to check unavailablity condition
        Zero_hotel.add_hotel()
        show.display("\t list of the Hotels available")
        show.display(Hotel.hotels)           # Display General details for all hotels
        show.display(Hayat_hotel.hotel_name) # Display the name for ONE hotel
    

        #Create instance objects for 4 customers 
        Saqr_Thabet=Reservation("Hayat","Saqr_thabet","+8613094449161")
        Ali_Ahmed=Reservation("Holydayin","Ali_ahmed","+8613094449161")
        Ameer_Nezar=Reservation("Holydayin","Ameer_nezar","+8613094449161")
        Galal_Taleb=Reservation("Zero","Galal_taleb","+8613228191565")

        #Create reservations for 4 customers
        if Saqr_Thabet.add_new_reservation():
            s_t=Customer(Saqr_Thabet.hotel_name,Saqr_Thabet.customer,Saqr_Thabet.number)
            s_t.add_customer()
            show.display(Saqr_Thabet.message)
            #show.display(Saqr_Thabet.reservations)
            #show.send_message(Saqr_Thabet.message,Saqr_Thabet.number)
    
        if Ali_Ahmed.add_new_reservation():
            m_a=Customer(Ali_Ahmed.hotel_name,Ali_Ahmed.customer,Ali_Ahmed.number)
            m_a.add_customer()
            show.display(Ali_Ahmed.message)
            #show.display(Ali_Ahmed.reservations)
            #show.send_message(Ali_Ahmed.message,Ali_Ahmed.number)
            
        if Ameer_Nezar.add_new_reservation():
            m_b=Customer(Ameer_Nezar.hotel_name,Ameer_Nezar.customer,Ameer_Nezar.number)
            m_b.add_customer()
            show.display(Ameer_Nezar.message)
            #show.display(Ameer_Nezar.reservations)
            #show.send_message(Ameer_Nezar.message,Ameer_Nezar.number)

    #def Test_reservation_disapproval():
        show.display("\t Test_reservation_disapproval ") 
        if Galal_Taleb.add_new_reservation():   # no rooms available 
            m_c=Customer(Galal_Taleb.hotel_name,Galal_Taleb.customer,Galal_Taleb.number)
            #show.display(Galal_Taleb.message)
            #show.display(Galal_Taleb.reservations)
            #m_a1.send_message(Galal_Taleb.message,Galal_Taleb.number)

        
    #def Test_misspelled_hotel_name():
        show.display("\t Test_misspelled_hotel_name ")
        Fagr_khalil=Reservation("Holyday","Fagr_Khalil","+8613094449161")
        Fagr_khalil.add_new_reservation()

    #def Test_delete_a_customer():
        show.display('\t Test_delete_a_customer')
        show.display(m_b.customer_list)        
        m_a.delete_customer()           # delete customer from customer Class
        show.display(m_b.customer_list)
        
    #def Test_reservation_removal():
        show.display('\t Test_reservation_removal')
        show.display(Ameer_Nezar.reservations)
        Ameer_Nezar.delete_a_reservation()   # delete customer booking from reswervation Class
        show.display(Ameer_Nezar.reservations)

    #def Test_delete_a_hotel():
        show.display('\t Test_delete_a_hotel')
        show.display(Hotel.hotels)
        Rotana_hotel.delete_hotel() 
        show.display(Hotel.hotels)

    #def Test_reservation_in_a_hotel(hotel):
        show.display("\t Test_reservation_in_a_hotel('Holydayin')")
        show.display(list_resevrations_for_hotel('Holydayin')) #from reservation.py
    
    #def Test_list_of_available_hotels_in_a_city(city):
        show.display("\t Test_list_of_available_hotels_in_a_city('Abu Dhabi')") 
        show.display(list_hotels_in_city('Abu Dhabi')) # from hotel.py
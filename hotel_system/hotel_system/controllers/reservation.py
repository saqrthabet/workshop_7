

"""
reservation.py
This is the Reservation class file
"""

from .hotel import Hotel


class Reservation():
    reservations=[]                                                 # defined here because, eventually I want an accumulation of the total reservations                                                      
    def __init__(self,hotel_name, customer_name,customer_number):
        self.hotel_name=hotel_name
        self.customer=customer_name
        self.number=customer_number
        #self.message=[]  # if  defined here,in order to have a unique output for each instance object, I get double results
    def __repr__(self):
        return f'Reservation({self.hotel_name!r}, {self.customer !r},{self.number !r})' 
     
    def add_new_reservation(self): # will face a problem if self.message=[]is defined above
        self.message=[]  # defined here,in order to have a unique output for each instance object,this instance variable will be assigned to Notification
        self.room_No=[]
        if reserve_room(self.hotel_name,self.customer):  # Add hotel_name, customer_name into the reservations list
            #self.room_No=hotel.empty_rooms   # defining the empty room, which will booked for the customer
            #Reservation.reservations.append(self.hotel_name,self.customer,self.number,self.room_No)
            #self.message.append(["Confirmation : Customer named under:"+str(self.customer)+" reserved Room.No: "+str(self.room_No)+" at "+str(self.hotel_name)+" Hotel"])
            Reservation.reservations.append(self)
            self.message.append(["Confirmation : Customer named under:"+str(self.customer)+" at "+str(self.hotel_name)+" Hotel"])
            return True                                               
        else:
            print("sorry no rooms available")
            return None
    def delete_a_reservation(self):
        #Reservation.reservations.remove([self.hotel_name, self.customer, self.number,self.room_No])  #Hotel.hotels[index_hotel][4] unkown value
        #self.room_No+=1         # how to update the No. of empty rooms at Hotel.hotels[index_hotel][4]+=1 e
        Reservation.reservations.remove(self)

def reserve_room(hotel_name,customer_name): 
    not_here=True
    for hotel in Hotel.hotels:
        if hotel.hotel_name != hotel_name:  # check the existance of hotel or spelling
            not_here=True
        else:
            not_here=False
            break
    if not_here:
        print("Sir,please check your spelling once more")
        return False
    else:
        is_here=False
        for otem in Reservation.reservations:  # check if there is a duplicate in the reservation
            if otem.hotel_name == hotel_name and otem.customer == customer_name:
                is_here=True
                break
            else:
                is_here=False
        if is_here:
            print("Sir,the reservation is already there")    
            return False
        else:
            if hotel.empty_rooms == 0:  #used for 2 purposes: check room availablity and list_reservations_for_hotel
                return False            #loop and check if there is empty_rooms in hotel_name  
            else:
                hotel.empty_rooms -=1            # update the empty rooms in hotel_name
                return True
                
def list_resevrations_for_hotel(hotel_name):
    list_reservation_for_that_hotel=[]
    not_here=True
    for hotel in Hotel.hotels:
        if hotel.hotel_name != hotel_name:  # check the existance of hotel or spelling
            not_here=True
        else:
            not_here=False
            break
    if not_here:
        print("Sir,please check your spelling once more")
        return False
    else:
        #for item in Reservation.reservations:  
            #if item.hotel_name != hotel_name:   # check the existance of hotel or spelling reservation list
            #print("we do not have a hotel with that name ")
            #return False
        in_reserve=False
        for reserv in Reservation.reservations:
            if reserv.hotel_name == hotel_name:
                in_reserve=True
                break
            else:                 #has no need 
                in_reserve=False  #has no need
        if in_reserve:
            #print("In "+str(hotel_name)+" Hotel "+"Customer named under "+str(Reservations.reservations[index_hotel][1])+" booked room number "+str(Reservations.reservations[index_hotel][3]))        
            list_reservation_for_that_hotel.append([hotel_name,reserv.customer]) # evade using reserv.room_no
    return list_reservation_for_that_hotel

"""
Initial_version( difference in indexing
     
    def add_new_reservation(self): # will face a problem if self.message=[]is defined above
        self.message=[]  # defined here,in order to have a unique output for each instance object,this instance variable will be assigned to Notification
        self.room_No=[]
        if reserve_room(self.hotel_name,self.customer):                         # Add hotel_name, customer_name into the reservations list
            self.room_No=Hotel.hotels[index_hotel][4]                           # defining the empty room, which will booked for the customer
            Reservation.reservations.append([self.hotel_name, self.customer, self.number,self.room_No])
            self.message.append(["Confirmation : Customer named under:"+str(self.customer)+" reserved Room.No: "+str(self.room_No)+" at "+str(self.hotel_name)+" Hotel"])
            #Reservation.message.append(["Confirmation : Customer named under:"+str(self.customer)+" reserved Room.No: "+str(Hotel.hotels[index_hotel][4])+" at "+str(self.hotel_name)+" Hotel"])
            return True                                                #add_new_reservation output will be assign to Notification()
            #print("capacity after reservaion");print(Hotel.hotels)
        else:
            print("sorry no rooms available")
            return None
    def delete_a_reservation(self):
        Reservation.reservations.remove([self.hotel_name, self.customer, self.number,self.room_No])  #Hotel.hotels[index_hotel][4] unkown value
        self.room_No+=1         # how to update the No. of empty rooms at Hotel.hotels[index_hotel][4]+=1 
            
def reserve_room(hotel_name,customer_name):
        hotels_names=[]
        for thing in Hotel.hotels:                         # primitive build list includes hotel_names
                hotels_names.append(thing[1])              # primitive
                
        if hotel_name not in hotels_names:                     # checking the Hotel name
            print("Sir,please check your spelling once more")
            return False
        else:                                            # else reserve a new room in hotel_name for customer_name
            global index_hotel
            index_hotel=[]
            index_hotel=hotels_names.index(hotel_name)            #used for 2 purposes: check room availablity and list_reservations_for_hotel
        if Hotel.hotels[index_hotel][4]==0:          # loop and check if there is empty_rooms in hotel_name
            return False
        else:
            Hotel.hotels[index_hotel][4]-=1            # update the empty rooms in hotel_name
            return True
def list_resevrations_for_hotel(hotel_name):
    hotels_names=[]
    list_reservation_for_that_hotel=[]
    hotels=[]
    for thing in Hotel.hotels:                     # primitive build list includes hotel_names
        hotels_names.append(thing[1])              # primitive          
    if hotel_name not in hotels_names:                     # checking the Hotel name
        print ("Sir, please check your spelling once more")
    else:
        for item in Reservation.reservations:  # primitive build list includes hotel_names
            hotels.append(item[0])          # primitive          
            if hotel_name not in  hotels:                      # checking the Hotel name
                print("we do not have a hotel with that name ")
            else:
                index_hotel=[]
                for index_hotel, j in enumerate(hotels):        #locate many indices not only one
                    if j == hotel_name:
                        #print("In "+str(hotel_name)+" Hotel "+"Customer named under "+str(Reservations.reservations[index_hotel][1])+" booked room number "+str(Reservations.reservations[index_hotel][3]))        
                        list_reservation_for_that_hotel.append([hotel_name,Reservation.reservations[index_hotel][1],Reservation.reservations[index_hotel][3]])
    return list_reservation_for_that_hotel
"""

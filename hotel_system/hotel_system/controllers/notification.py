"""
    notifications.py
    This is the main application file for the Hotel Reservation system 
"""
#from twilio.rest import Client

class Notifications:
    #def __init__(self)

    def display(self,message):
        self.message=message
        #print(str(self.message))
        print (self.message)
        #print(list(self.message))  #list is added, as its not a simple list because returned object is not a list.
"""
    def send_message(self,message,customer_number): # how to deal with hotel_name & customer_name
        self.message=message
        self.customer_number=customer_number
        #def send_text_message(customer_name,customer_number,hotel_name):
        # Your Account Sid and Auth Token from twilio.com/console
        account_sid = "AC40bbdd8861ae0e37ef0ab3ed22eb69f5"
        auth_token = "b09e23bb114453a802726bd82f3aba52"        
        client = Client(account_sid, auth_token)
        #message = client.messages.create(body="Dear Mr/Madam: "+str(customer_name)+" we confirm your booking at "+str(hotel_name)+" Hotel",to=customer_number,from_="+18553427622")
        message = client.messages.create(body=message,to=customer_number,from_="+18553427622")
        print(message.sid)
"""    

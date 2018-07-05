
"""
customer.py
This is the Customer class file 
"""

class Customer():
    customer_list=[]
    #def add_customer(self,hotel_booked,customer_name,customer_number):
    def __init__(self,hotel_booked,customer_name,customer_number):
        self.hotel_booked=hotel_booked
        self.name=customer_name
        self.number=customer_number
    def __repr__(self):
        return f'Customer({self.hotel_booked!r}, {self.name !r},{self.number !r})'
        
    def check_if_duplicate(self): # check whether customer is a duplicate or not
        existed= False
        for customer in Customer.customer_list:
            if customer.name == self.name and customer.number == self.number:
                existed = True
        return existed
        
    def add_customer(self):
        if not self.check_if_duplicate():
            Customer.customer_list.append(self)

    def delete_customer(self):
        for customer in Customer.customer_list:
            if customer.name == self.name and customer.number == self.number: # jump over list elements
                Customer.customer_list.remove(customer)  # delete the(list) indicates to specific instance object
                #Customer.customer_list.remove([self.name, self.number,self.hotel_booked])


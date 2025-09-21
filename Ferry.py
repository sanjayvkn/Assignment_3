'''Create Ferry Booking'''
# global ticket ID (Whenever someone makes a new booking  the count goes up by one)
Ticket_ID = 1000
# This is Booking System Class 
class BookingSystem:
    # I Created the list for all the Bookings
    all_bookings = []
    def __init__(self):
        global Ticket_ID
        #Each booking stores its own numbers separately.
        self.approval = 0
        self.Not_Approved = 0
        self.Pending = 0
        Ticket_ID +=1 # give each booking a new unique ID
        # detials of booking
        self.ID_Number = "" 
        self.Name = ""
        self.customer_ID = Ticket_ID
        self.Total_price = ""
        self.status = "Pending"
        self.reference_num = "None"
        # Add booking into the list
        BookingSystem.all_bookings.append(self)
    # Enter the details 
    def customer_info(self):
        self.ID_Number= input("Enter Number ID: ")
        self.name = input("Enter Passager Name: ")
    # Ferry service detalis 
    def ferry_service_details(self):
        try:
            self.Ferry_name = input("Enter Ferry name: ")
            self.Ticket_cost = float(input("Enter the price item($): "))
            self.Ticket_cost+= self.Ticket_cost 
        except ValueError : 
            print("Error") 
     # Manager approval (yes/no)
    def Manager_approval(self):
        self.approval = input("Enter Manager approval Y or N :").lower()
        if self.approval == "y":
            self.status = "Approved"
            reference_num = self.ID_Number[:3] + str(self.customer_ID)
            print(reference_num)
        else  :
            self.status = "Not Approved"
            reference_num = None
    # display the details customer 
    def display_booking_info(self):
        print("\n Printing Ferry")
        print("Number id:", self.ID_Number)
        print("name:",self.Name)
        print("Customer id:", self.customer_ID)
        print("status:", self.status)
        print("Total: $", self.Total_price)
    # Show booking statistics 
    def booking_statistics(self):
        total = len(BookingSystem.all_bookings)

        for Fry in BookingSystem.all_bookings:
            if Fry == "Approved":
                self.approval +=1
            elif Fry == "Not approved":
                self.Not_Approvel +=1
            elif Fry == "Pending":
                Pending +=1
        print("\nthe booking statistics:")
        print(f"The total number of bookings submitted:{total}")
        print(f" The total number of approved bookings:{self.approval}")
        print(f" The total number of pending bookings:{self.Not_Approvel}")
        print(f" The total number of not approved bookings:{Pending}")
# this calling function 
if __name__ == "__main__":
    while True:
        Ferry1 = BookingSystem()
        Ferry2 = BookingSystem()
        Ferry3 = BookingSystem()
        Ferry4 = BookingSystem()
        Ferry5 = BookingSystem()
        
# Run functions
        Ferry1.customer_info()
        Ferry2.ferry_service_details()
        Ferry3.Manager_approval()
        Ferry4.display_booking_info()
        Ferry5.booking_statistics()
        break # end of loop 
    
     

    






            
    
    
    

    
    
        

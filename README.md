# Assignment_3
software practical work 
                             IT5016 
                     Assignment Part 3
              IT Technical Fundamentals 









    
Name: Sanjay 
Student ID : 20250184
          Assessment 3: principle and concepts


	
 
Project of Ferry System Booking:

This is my project about Ferry booking system as You have hear booking system that means booking something for services. I have used the python for Booking system. It was created as a small learning project to practice how classes, objects, and methods work together in programming. The main goal is not to build the realistic Booking system but learn and practice the coding principals. As I have learn and implemented on my code. 

Intent of the System
The Ferry Booking System helps us:
•	Enter customer details
•	Add ferry service details (like ferry name and ticket price)
•	Approve or reject bookings with manager input
•	Display the booking information
•	Show booking statistics (approved, pending, not approved)
Each booking is stored separately with its own unique ID number. This makes sure no two bookings are the same.
How it Works
Unique Ticket ID
A global ticket ID starts at 1000.
Every time a new booking is created, the ID number increases by one.
Example : It is the start number as I have used the Ticket_ID = 1000
After that,
I have make the class for the booking system to run all the program in that single code.
Example: class BookingSystem:
Customer Information
The program asks the user for an ID number and passenger name.
Example: This is the customer information that system wants like:
  def customer_info(self):
        self.ID_Number= input("Enter Number ID: ")
        self.name = input("Enter Passager Name: ")

Ferry Service Details
The user types the ferry name and ticket price.
If the price entered is not a number, the program shows an error Because we have given the float. 
    def ferry_service_details(self):
        try:
            self.Ferry_name = input("Enter Ferry name: ")
            self.Ticket_cost = float(input("Enter the price item($): "))
            self.Ticket_cost+= self.Ticket_cost 
        except ValueError : 
            print("Error") 

Manager Approval
The manager enters “Y” (yes) or “N” (no).
Approved bookings get a reference number made from the ID.
Not approved bookings are marked as “Not Approved.”
    def Manager_approval(self):
        self.approval = input("Enter Manager approval Y or N :").lower()
        if self.approval == "y":
            self.status = "Approved"
            reference_num = self.ID_Number[:3] + str(self.customer_ID)
            print(reference_num)


Display Information
The booking information is shown on the screen, including name, ID, status, and total price.
    def display_booking_info(self):
        print("\n Printing Ferry")
        print("Number id:", self.ID_Number)
        print("name:",self.Name)
        print("Customer id:", self.customer_ID)
        print("status:", self.status)
        print("Total: $", self.Total_price)

Statistics
The system counts how many bookings are approved, pending, or not approved.
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
 Principles Used
•	KISS (Keep It Simple, Stupid):
The code is kept short and simple. Only the essential features are added, so it is easy to understand.
•	Open/Closed Principle:
The program is open for adding new features (like more booking options), but closed for changes to the basic structure. For example, you can add new methods without rewriting the main booking class.
•	Single Responsibility Principle:
Each method has one clear job. For example, customer_info() only collects customer details, while Manager_approval() only deals with approval.
<img width="468" height="537" alt="image" src="https://github.com/user-attachments/assets/14fc9953-895b-46dc-8835-80b1a5151d78" />

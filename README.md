                                           Report

                              
                           Software development fundamentals

                                                
                                                IT5016


    Name: Sanjay
 Student ID : 20250184
                           Due date : 02/10/2025
            Assessment 3: principle and concepts











Introduction:
This project is a Ferry Booking System made with Python. The main purpose of this project is to practice and understand how classes, objects, methods, and variables work together. A booking system usually means reserving something for a service, and here it is shown in a simple code example. The project is not a full or realistic booking system, but a learning exercise. It uses basic coding principles like keeping the code simple, avoiding repetition, using a class for logic, and storing data in lists. By doing this project, I learned how coding principles work together to make code more organized, reusable, and easy to read. It also gave me hands-on experience with object-oriented programming and how software design ideas can help in building better programs.
 Analysis:
The main objective of this project is to manage ferry bookings in a simplified way.  
It includes the following features:
Automatic assignment of unique Booking IDs.
Tracking of Approved and Not Approved bookings.
Central storage of all bookings for display and retrieval.
Although small in scope, the system highlights the importance of applying software design principles to achieve clean, maintainable, and extendable code.
Software Design Principles Used
 K.I.S.S (Keep It Simple, Stupid)
The system avoids unnecessary complexity and used a simple class structure with attributes and methods.
D.R.Y (Don't Repeat Yourself)
Shared booking data is stored in a single list (`all_bookings`) instead of duplicating records in multiple places.
Single Responsibility Principle

The `BookingSystem` class handles booking-related tasks such as creation, approval, and tracking.  
Each method has a clear, single responsibility.
Separation of Concerns

While basic, the design separates responsibilities:  
 The global variable manages ID generation.  
  The class manages booking logic and records.
Clean Code > Clever Code

Code readability and clarity over complex or solutions.  
  For example, clear variable names like `approval` and `Not_Approved` are used.
 Software Design Principles Not Fully Used
Open / Closed Principle
The system is not fully extendable without modifying the class. Adding new booking features requires direct changes.
Composition Over Inheritance
No composition or modular objects are created, as everything is managed within a single class.
Y.A.G.N.I (You Aren't Gonna Need It)
Some basic placeholders exist (like counters) that may not be strictly necessary for the current system.
Refactor, Refactor, Refactor
The project lacks iterative refactoring stages; improvements such as splitting the code into multiple files have not been applied.
Avoid Premature Optimisation
Optimisation techniques (such as database storage, caching, or advanced algorithms) have not been considered, which is acceptable for a learning project.
Notice: it has the problem of plagiarism because of that I have done and my file also I am mentioning my readme file in the end of this.
<img width="468" height="623" alt="image" src="https://github.com/user-attachments/assets/ab6c9f69-0b78-4aa3-b996-68bf4096fd71" />

<img width="468" height="623" alt="image" src="https://github.com/user-attachments/assets/e33afaf0-726d-4a87-873d-aac72fecf686" />


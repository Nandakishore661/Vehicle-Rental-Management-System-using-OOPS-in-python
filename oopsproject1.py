# Mini Project: Vehicle Rental Management System
# Scenario


# A vehicle rental company rents cars and bikes to customers. The company needs a Python application to manage vehicles, customer rentals, rental charges, and vehicle availability.
# Students must design the application using all four pillars of OOP: Encapsulation, Inheritance, Abstraction, and Polymorphism.
# The project should be developed using classes and objects. Do not use a database or GUI initially; students can store data in lists and interact through a menu-driven console application.
# Project requirements
# The application should provide the following menu:
# ===== Vehicle Rental Management System =====

# 1. Display Available Vehicles
# 2. Register a Customer
# 3. Rent a Vehicle
# 4. Return a Vehicle
# 5. Calculate Rental Charges
# 6. Display Rental Details
# 7. Exit
# How each OOP pillar connects to the project



# 1. Encapsulation – Protect vehicle and rental information
# The company should control how important information is accessed or updated.
# Students must:
# Store the vehicle's rental price and availability using private-style attributes.
# Store customer information such as customer ID and contact details.
# Provide methods to display or update vehicle availability.
# Prevent rental availability from being changed directly outside the relevant methods.





# Scenario: When a customer rents a car, the vehicle should become unavailable. When the customer returns it, the vehicle should become available again.

# 2. Inheritance – Manage different types of vehicles
# Create a common parent class named Vehicle.
# Create the following child classes:
# Car
# Bike
# The parent class should contain common vehicle information, such as:
# Vehicle ID
# Brand
# Model
# Rental price per day
# Availability
# Each child class should inherit the common features and provide its own additional information.
# For example:
# A car may have a seating capacity.
# A bike may have an engine capacity.
# Scenario: The company should not need to write the same vehicle registration and display functionality separately for cars and bikes.




# 3. Abstraction – Define the rental process
# Create an abstract class named Rentable that defines the required rental operations.
# Students must decide which operations every rentable vehicle must support, such as:
# Renting a vehicle
# Returning a vehicle
# Calculating rental charges
# The child classes should implement the required abstract methods.
# Scenario: The rental system should be able to request rental charges without knowing the internal calculation process of each vehicle type.



# 4. Polymorphism – Calculate different rental charges
# Different vehicle types may have different rental charges.
# Students must implement a common method named calculate_rent() in the vehicle classes.


# For example:
# A car's rental charge may depend on the number of rental days and a fixed daily rate.
# A bike's rental charge may depend on the number of rental days and its daily rate, with an additional helmet rental charge if applicable.
# The system should call the same method for both types of vehicles and receive the appropriate result.
# Scenario: When the company calculates the rental amount, it should not need separate menu operations for cars and bikes.




# Functional requirements
# Students must implement these operations:
# Register at least five vehicles, including cars and bikes.
# Display all available vehicles.
# Register customers with unique customer IDs.
# Allow a customer to rent an available vehicle.
# Prevent renting a vehicle that is already rented.
# Record the rental date and expected return date.
# Calculate rental charges based on the vehicle type and rental duration.
# Return a vehicle and update its availability.
# Display the rental history of a customer.
# Display the total rental amount for a completed rental.




# Sample scenario for testing
# A customer named Ravi wants to rent a car for three days.
# The system should:
# Display available cars.
# Allow Ravi to select a car.
# Mark the selected car as unavailable.
# Calculate the rental amount for three days.
# Record the rental details.
# When Ravi returns the car, mark it as available again.
# Students should also test what happens when Ravi attempts to rent the same car a second time before returning it.
# Student deliverables
# A class diagram showing the parent class, child classes, and their relationships.
# Python source code with appropriate classes and methods.
# A menu-driven console application.
# At least five test scenarios, including invalid rental attempts and vehicle returns.
# A short explanation of where each of the four OOP pillars is used and how they work together.




# 1. Encapsulation – Protect vehicle and rental information
print("1. Encapsulation")


class vehicle:
    def __init__(self , vehicle_id , brand , price):
        self.vehicle_id = vehicle_id
        self.brand =  brand
        
        #using private 
        self.__price = price
        self.__available = True
        
    def display_vehicle(self):
        print("vehicle_id;", self.vehicle_id)
        print("Brand:", self.brand)
        print("Rented price:", self.__price)
        print("Available:", self.__available)
        
    def get__price(self):
        return self.__price
    
    def is_available(self):
        return self.__available
    
    def rent_vehicle(self):
        if self.__available:
            self.__available = False
            print('vehicle is rented successfully')
        else:
            print("vehicle is already rented..")
    
    def return_vehile(self):
        if not self.__available:
            self.__available = True
            print("vehicle is returned successfully..")
        else:
            print("vehile was not returned..")
            
# Create an object
v1 = vehicle("C101", "Maruti", 1500)

v1.display_vehicle()

v1.rent_vehicle()
print("Available:", v1.is_available())

v1.return_vehile()
print("Available:", v1.is_available())
    
print("\n")

print("2. Inheritance")

# 2. Inheritance – Manage different types of vehicles

class vehicle:
    def __init__(self, vehicle_id, brand, model, price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.price = price
        
    def display(self):
        print("vehicle_id:", self.vehicle_id)
        print("Brand:", self.brand)
        print("vechile_model:", self.model)
        print("vehicle price:", self.price)
    
    
class car(vehicle):
    def __init__(self, vehicle_id, brand, model, price, seats):
        super().__init__(vehicle_id, brand, model, price)
        self.seats = seats
        
    def display(self):
        super().display()
        print("seats capacity:", self.seats)
        
class bike(vehicle):
    def __init__(self, vehicle_id, brand, model, price,engine_cc):
        super().__init__(vehicle_id, brand, model, price) 
        self.engine_cc = engine_cc
    
    def display(self):
         super().display()
         print("Engine Capacity:", self.engine_cc, "CC")

car = car("1478", "TOYOTA" ,"Fortuner" , 1500 , 5 )
bike = bike("8791" ,"Royal Enfield" , "GT-650" , 1000, 650)

print("--car details--")
car.display()

print("\n--bike details--")
bike.display()

print("\n")

print("3. Abstraction")




# 3. Abstraction – Define the rental process

from abc import ABC, abstractmethod

class rentable(ABC):
    
    @abstractmethod
    def rent_vehicle(self):
        pass
    
    @abstractmethod
    def return_vehicle(self):
        pass
    
    @abstractmethod
    def calculate_rent(self, days):
        pass

class car(rentable):
    def __init__(self, price):
        self.price = price
        self.available = True
    
    def rent_vehicle(self):
        if self.available:
            self.available= False
            print("Car rented successfully.")
        else:
            print("Car is already rented.")
    
    def return_vehicle(self):
        if not self.available:
            self.available = True
            print("Car returned successfully.")
        else:
            print("Car was not rented.")
    
    
    def calculate_rent(self, days):
        return self.price * days
    
car = car(1500)
car.rent_vehicle()
amount = car.calculate_rent(3)
print("Three-day rental charge:", amount)

car.return_vehicle()
print("\n")

print("4..Polymorphism")

# 4. Polymorphism – Calculate different rental charges

class car:
    def __init__(self, price):
        self.price = price
        
    def calculate_rent(self , days):
        return self.price * days

class bike:
    def __init__(self, price):
        self.price = price
    
    def calculate_rent(self,days):
        helmate_charge = 50 * days
        return self.price * days + helmate_charge

car = car(1500)
bike =bike(500)

# Same method, different behavior
vechicles = [car , bike]

for vehicle in vechicles:
    amount = vehicle.calculate_rent(3)
    print("Rental charge:", amount)
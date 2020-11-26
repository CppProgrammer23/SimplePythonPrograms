#Create a Vehicle class with name, max_speed and mileage instance attributes
class Vehicle:
    color='White'
    def __init__(self,name,max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    def fare(self,capacity):
        return capacity*100
myInst=Vehicle('BMW',260,1500)
#print(myInst.max_speed, myInst.mileage)
######################################################

#Create a Vehicle class without any variables and methods
class Vehiclee:
    pass
###########################################

#Create child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity)
    def fare(self,capacity=50):             #def fare(self,capacity=50):
        amount = super().fare(capacity)             #return super().fare(capacity+capacity*10/100)
        return amount+amount*10/100
myBus=Bus('Volvo',220,1400)
print('the vehicle name\'s: ',myBus.name,', its max speed is: ',myBus.max_speed, ' and its mileage is: ',myBus.mileage)
print(myBus.seating_capacity())
###########################################

#Define property that should have the same value for every class instance
class Car(Vehicle):
    pass
myCar=Car('Audi',260,1420)
myBuus=Bus('Volvo',180,2500)
print(myCar.color); print(myBuus.color)

#verify if a instance is an instance of Bus is also an instance of Vehicle 
print(isinstance(myBuus,Vehicle))

#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating 
#capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
#So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
print(myBuus.fare())

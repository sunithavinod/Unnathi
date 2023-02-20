class vehicle:
    def seating(self,capacity,maintanance):
        self.capacity=capacity
    def fare(self):
        n=int(input("enter the capacity"))
        if(n<=50):
            self.f= self.capacity*100
            print("the total fare charges is",self.f)
        elif(n>=50):
            self.total= (self.capacity*100)+0.1
            print("vehicle is bus instance so extra 10% added for maintenance")
            print("total is",self.total)
        else:
            print("invalid")
class Bus(vehicle):
    def seating(self, capacity,maintanance):
       vehicle.seating(self, capacity, maintanance)
b1=Bus()
b1.seating(50,10)
b1.fare()

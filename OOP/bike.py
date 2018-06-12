class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def drive(self):
        self.miles += 10
        # print ("Total bike miles is now {}".format(self.miles))
        print ("Riding")
        # return self
    
    def displayInfo(self):
        print "Total price is $" + str(self.price)
        print "Max speed is " + str(self.max_speed) + "mph"
        print "Total miles is " + str(self.miles) + " miles"
    
    def reverse(self):
        print ("Reversing")
        self.miles -= 5
        # if self.miles >= 5:
            # self.miles -= 5

Yamaha=Bike(27999,50)
Yamaha.drive()
Yamaha.drive()
Yamaha.drive()
Yamaha.reverse()
Yamaha.displayInfo()

harley=Bike(32998, 120)
harley.drive()
harley.drive()
harley.reverse()
harley.reverse()
harley.displayInfo()


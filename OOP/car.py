class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    
    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: $" + str(self.tax)

range_rover=Car(75000,56,"Full",15)
# range_rover.display_all()
tesla=Car(35000,80,"Hybrid", 35)
accord=Car(32000,80,"Full",30)
lexus_gs=Car(29000,85,"Half full", 28)
bmw=Car(38000,78,"Partially full", 26)
scion=Car(25000,70,"Almost empty",27)
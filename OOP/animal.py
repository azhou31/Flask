class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 10
        # self.status = "Healthy"
    
    # def mobility(self, status):
    #     if status == "walk":
    #         self.health -= 1
    #         self.status = "Good"
    #     if status == "run":
    #         self.health -= 5
    #         self.status = "Exhausted"
    #     print "Health score is: " + str(self.health)
    #     print "Health status is: " + str(self.status)

    def walk(self):
        self.health -= 1

    def run(self):
        self.health -= 5
    
    # def displayHealth(self):
    #     print str(self.health)

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self). __init__(name)
        self.health = 150

    def pet(self):
        self.health += 5

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        self.health -= 10


tiger=Animal("Bob")
tiger.walk()
tiger.walk()
tiger.walk()
tiger.run()
tiger.run()
print "Health: " + str(tiger.health)

d=Dog("Yogi")
d.walk()
d.walk()
d.walk()
d.run()
d.run()
d.pet()
print "Health: " + str(d.health)

D=Dragon("Hoover")
print D.health
print "I am a Dragon"

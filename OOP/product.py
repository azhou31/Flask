class Product(object):
    def __init__(self,price,item_name,weight,brand,cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
        self.tax = 0.15

        # if self.status == "defective":
        #     self.status = "defective"
        #     self.price = 0

    def displayInfo(self):
        print "Price: $" + str(self.price + self.tax)
        # print "Price: $:" + str(self.price) + str(self.tax)
        # print "Price: $" + [str(self.price)+str(self.tax)]
        print "Item Name: " + str(self.item_name)
        print "Weight: " + str(self.weight) + "oz"
        print "Brand: " + str(self.brand)
        print "Cost: $" + str(self.cost)
        print "Status: " + str(self.status)
    
    def return_item(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "in_box":
            self.status = "For Sale"
        if reason == "opened":
            self.price = self.price * 0.8
            self.status ="Used"



cream=Product(11.99,"foundation cream",1,"sephora",3.15)
cream.displayInfo()
cream.return_item("opened")
cream.displayInfo()
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name

    def read_odometer(self):
        print("这辆车已经行驶了"+str(self.odometer)+"公里")

    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("你不能把里程回调")

    def increment_odometer(self,miles):
        self.odometer += miles

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
        print("这辆车有" + str(self.battery_size) + "千瓦时容量的电池")

    def update_battery_size(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "这辆车大概可以走"+str(range)+"英里"
        print(message)

class Electriccar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()


electriccar = Electriccar(" "," "," ")
electriccar.battery.range()
electriccar.battery.update_battery_size()
electriccar.battery.range()






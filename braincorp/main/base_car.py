from stats import Stats
from gear import GEAR

class Base_Car:
    def __init__(self):
        self.maximun_speed = 50
        self.accelaration = 5
        self.brake_efficiency = -10
        self.distance = 0
        self.home_distance = 0
        self.speed = 0
        self.car_on = False
        self.headlights = False
        self.current_gear = GEAR.PARK

    def on(self): 
        self.car_on = True
        self.home_distance = 0
    
    def off(self):
        if self.get_speed() == 0:
            self.car_on = False
    
    def is_car_on(self): 
        return self.car_on

    def lights(self):
        self.headlights = True

    def lights_off(self):
        self.headlights = False

    def get_lights(self):
        return self.headlights

    def set_speed(self, speed):
        self.speed = speed
        if self.speed == 0:
            self.current_gear = GEAR.PARK
        else:
            self.current_gear = GEAR.FORWARD

    def get_speed(self): 
        return self.speed
    
    def get_distance(self): 
        return self.distance
    
    def get_home_distance(self): 
        return self.home_distance

    def gear(self, gear):
        if self.speed == 0:
            self.current_gear = gear

    def get_gear(self):
        return self.current_gear

    def gas(self, time):
        if self.is_car_on():
            newSpeed = self.get_speed() + self.accelaration * time
            newSpeed = min(max(newSpeed, 0), self.maximun_speed)
            self.set_speed(newSpeed)

    def brake(self, time):
        if self.is_car_on():
            newSpeed = self.get_speed() + self.brake_efficiency * time
            newSpeed = min(max(newSpeed, 0), self.maximun_speed)
            self.set_speed(newSpeed)

    def drive(self, time): 
        if self.is_car_on():
            self.distance += time * self.speed
            self.home_distance += time * self.speed

    def stats(self):
        stats = Stats()
        stats.set_stats(self.distance, self.home_distance, self.headlights, self.car_on, self.speed, self.current_gear)
        print(stats.check_stats())
        return stats.check_stats()




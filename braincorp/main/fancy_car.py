from base_car import Base_Car
from gear import GEAR

class FancyCar(Base_Car):
    def __init__(self):
        super().__init__()
        self.previous_gear = GEAR.FORWARD
        self.maximun_speed = 100

    def set_speed(self, speed):
        self.speed = speed
        if self.speed == 0:
            self.current_gear = GEAR.PARK
        else:
            self.current_gear = self.previous_gear

    def drive(self, time):
        if self.is_car_on():
            self.distance += time * self.speed
            if self.get_gear() == GEAR.FORWARD:
                self.home_distance =  self.home_distance + time * self.speed
            elif self.get_gear() == GEAR.REVERSE:
                self.home_distance =  self.home_distance - time * self.speed

    def gear(self, gear):
        if self.speed == 0:
            if gear == 'drive':
                self.current_gear, self.previous_gear = GEAR.FORWARD, GEAR.FORWARD
            elif gear == 'reverse':
                self.current_gear, self.previous_gear = GEAR.REVERSE, GEAR.REVERSE              

    def horn(self):
        print("beep beep")
        return "beep beep"
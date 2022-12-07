from gear import GEAR

class Stats:
    def __init__(self):
        self.engine = False
        self.headlights = False
        self.speed = 0
        self.distance = 0
        self.home_distance = 0
        self.current_gear = GEAR.PARK

    def set_stats(self, distance, home_distance, headlights, engine, speed, current_gear):
        self.distance = distance
        self.home_distance = home_distance
        self.headlights = headlights
        self.engine = engine
        self.speed = speed
        self.current_gear = current_gear

    def check_stats(self):
        return ("engine: " + str(self.engine) + ", lights: " + str(self.headlights) + ", speed: " + str(self.speed) + " m/s" + ", odometer: "+ str(self.distance) +  " m" + ", home: " + str(abs(self.home_distance)) + " m" +", gear: " + str(self.current_gear))


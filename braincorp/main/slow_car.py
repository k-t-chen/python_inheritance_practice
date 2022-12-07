from base_car import Base_Car

class SlowCar(Base_Car):
    def __init__(self):
        super().__init__()
        self.accelaration = 3.75
        self.maximun_speed = 37.5
        self.brake_efficiency = -20  
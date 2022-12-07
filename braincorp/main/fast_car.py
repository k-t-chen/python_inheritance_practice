from base_car import Base_Car

class FastCar(Base_Car):
    def __init__(self):
        super().__init__()
        self.accelaration = 10
        self.maximun_speed = 150
        self.brake_efficiency = -10   

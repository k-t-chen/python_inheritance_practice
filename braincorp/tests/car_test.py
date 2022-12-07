import sys
sys.path.append("main")
from fancy_car import FancyCar
from fast_car import FastCar

car_1 = FastCar()
car_1.on()
car_1.gas(1)
car_1.drive(10)
car_1.brake(3)
car_1.off()
car_1.stats()


car_2 = FancyCar()
car_2.lights()
car_2.on()
car_2.gear('reverse')
car_2.gas(1)
car_2.drive(10)
car_2.stats()
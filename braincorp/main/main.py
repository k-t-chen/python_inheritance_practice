from fancy_car import FancyCar
from fast_car import FastCar
from slow_car import SlowCar


def main():
    fastCar = FastCar()
    fancyCar = FancyCar()
    slowCar = SlowCar()
    fastCar.on()
    fancyCar.on()
    slowCar.on()
    fastCar.lights()
    fancyCar.lights()
    fastCar.gas(11)
    fancyCar.gas(11)
    slowCar.gas(11)
    fastCar.drive(30)
    fancyCar.drive(30)
    slowCar.drive(30)
    fancyCar.brake(5)
    fancyCar.drive(3)
    slowCar.brake(6)        
    fancyCar.brake(1)
    fancyCar.gear('reverse')       
    fancyCar.gas(20)
    fancyCar.drive(30)
    slowCar.off()
    fancyCar.lights_off()        
    fastCar.drive(30)
    fastCar.gas(20)
    fastCar.drive(60)
    fastCar.stats()
    fancyCar.stats()
    slowCar.stats()
    fancyCar.horn()
    fancyCar.horn()
    slowCar.on()
    slowCar.lights_off()
    slowCar.gas(4)
    slowCar.drive(2000)
    slowCar.stats()


if __name__ == "__main__":
    main()
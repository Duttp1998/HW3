class Car:

    def __init__(self):
        self.__maxprice = 20000

    def sell(self):
        print('Encapsulation Selling Price: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


vehicle = Car()
vehicle.sell()

vehicle.__maxprice = 20000
vehicle.sell()

vehicle.setMaxPrice(20000)
vehicle.sell()
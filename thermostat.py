import matplotlib.pyplot as plt, random

class Thermostat:
    __power = 0.5
    __heat = False
    __cool = False

    def __init__(self, temperature, min, max):
        self.temperature = temperature
        assert(min < max)
        self.min = min
        self.max = max

    def get_temperature(self, temperature):
        self.temperature = temperature

        if self.temperature < self.min:
            self.__heat = True
        elif self.temperature > self.max:
            self.__cool = True

        if self.__heat and self.temperature > (self.min + self.max)/2:
            self.__heat = False
        elif self.__cool and self.temperature < (self.min + self.max)/2:
            self.__cool = False

        if self.__heat:
            self.heating()
        elif self.__cool:
            self.cooling()

    def heating(self):
        self.temperature += self.__power

    def cooling(self):
        self.temperature -= self.__power


if __name__ == '__main__':
    test = Thermostat(35, 20, 25)
    plot_list = []
    
    for i in range(1000):
        if i % 100 == 0:
            test.temperature = 30
        if i % 200 == 0:
            test.temperature = 15
        plot_list += [test.temperature]
        test.get_temperature(test.temperature + random.random() - 0.5)

    plt.plot(plot_list)
    plt.show()

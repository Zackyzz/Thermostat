import matplotlib.pyplot as plt, random

class Thermostat:
    __heat = False
    __cool = False

    def __init__(self, temperature, min, max, temperature_variance):
        self.temperature = temperature
        assert(min < max)
        self.min = min
        self.max = max
        self.power_variance = 2*temperature_variance #the heating/cooling is twice more powerful than the temperature variance
        self.temperature_variance = temperature_variance

    def set_temperature(self, temperature):
        self.temperature = temperature

        if self.temperature < (self.min + self.temperature_variance):
            self.__heat = True
        elif self.temperature > (self.max - self.temperature_variance):
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
        self.temperature += self.power_variance

    def cooling(self):
        self.temperature -= self.power_variance


class Sensor:
    __temperature_variance = 0.3 #default variation of temperature between two time-steps
    temperature_history = []

    def __init__(self, min, max):
        self.thermostat = Thermostat(random.randint(min, max), min, max, self.__temperature_variance)

    def run_time_steps(self, time_steps):
        for i in range(time_steps):
            self.temperature_history += [self.thermostat.temperature]
            self.thermostat.set_temperature(self.thermostat.temperature + self.__temperature_variance*(random.random() - 0.5)/0.5)



if __name__ == '__main__':
    test_sensor = Sensor(20, 25)
    test_sensor.run_time_steps(1000)

    plt.plot(test_sensor.temperature_history)
    plt.show()

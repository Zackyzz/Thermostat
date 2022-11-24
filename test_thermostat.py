import unittest
from thermostat import Interface

def between(n, a, b):
    if n < a or n > b:
        return 1
    return 0

class TestThermostat(unittest.TestCase):
    def testTemperatureInRange(self):
        test_thermostat = Interface(20, 25)
        test_thermostat.run_time_steps(1000)
        in_range = map(lambda x: between(x, 20, 25), test_thermostat.temperature_history)
        self.assertEqual(sum(in_range), 0)

    def testTemperatureOutOfRange(self):
        test_thermostat = Interface(20, 25)
        test_thermostat.run_time_steps(1000)
        in_range = map(lambda x: between(x, 22, 23), test_thermostat.temperature_history)
        self.assertGreater(sum(in_range), 0)
    
    def testInterfaceInput(self):
        with self.assertRaises(ValueError):
            Interface(21, 20)
        with self.assertRaises(AssertionError):
            Interface(20, 20)
        with self.assertRaises(ValueError):
            Interface(21.1, 22.1)
  
if __name__ == '__main__':
    unittest.main()
 
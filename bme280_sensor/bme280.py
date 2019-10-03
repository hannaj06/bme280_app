import bme280
import smbus2
from time import sleep


class bme280_sensor:

    def __init__(self, port=1, address=0x77):
        self.port = port
        self.address = address
        self.bus = smbus2.SMBus(self.port)
        bme280.load_calibration_params(self.bus, self.address)

    def read(self, sysout=False):
        bme280_data = bme280.sample(self.bus, self.address)

        env_data = {
            'temp_f': self.formater(bme280_data.temperature * 9/5 + 32),
            'temp_c': self.formater(bme280_data.temperature),
            'humidity': self.formater(bme280_data.humidity),
            'pressure': self.formater(bme280_data.pressure),
            'ts': bme280_data.timestamp
            }
        
        if sysout==True:
            print('''
            Temperature:  {temp_c} c, {temp_f} F    
            Humidity: {humidity}% rH
            Pressure: {pressure} hPa
            '''.format(**env_data))
        
        return env_data


    @staticmethod
    def formater(value, n=2):
        return round(value,n)
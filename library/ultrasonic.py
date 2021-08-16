#Libraries
import RPi.GPIO as GPIO
import time
 

class Sonic():
    
    def init(self, GPIO_TRIGGER = 18, GPIO_ECHO = 24):
        GPIO.setmode(GPIO.BCM)
        #set GPIO Pins
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO
        
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
    
    def measure_distance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, GPIO.HIGH)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.0001)
        GPIO.output(self.GPIO_TRIGGER, GPIO.LOW)
        
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance

    def convert_distance_to_percentage(self, distance):
        return int((35.0 - distance) / 30.0 * 100.0) if int((35.0 - distance) / 30.0 * 100.0) > 0 else 0
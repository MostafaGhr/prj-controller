import RPi.GPIO as GPIO          
import time
class Motor():
    def __init__(self, in1=24, in2=23, en=25):
        '''
        intializes the motor class
        and sets the pins to be outputs
        and sets the en pin for pwm to control motor speed
        '''
        self.in1 = in1
        self.in2 = in2
        self.en = en
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(en,GPIO.OUT)

        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

        p = GPIO.PWM(en,1000)

        p.start(25)

        # set speed
        p.ChangeDutyCycle(100)


        GPIO.setmode(GPIO.BCM)

    def open_door(self):
        '''
        calling this function will open the door
        '''
        print("opening door")
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        time.sleep(1.17)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

    def close_door(self):
        '''
        calling this function will close the door
        '''
        print("closing door")
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        time.sleep(1.1)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

    def rotate(self, value):
        '''
        using this function will rotate motor in a given direction
        using positive values will rotate clockwise
        using negative values will rotate counterclockwise
        '''
        if value > 0:
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
        elif value < 0:
            value = value * -1
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
        time.sleep(value/10)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

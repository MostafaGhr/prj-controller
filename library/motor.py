import RPi.GPIO as GPIO          
import time

in1 = 24
in2 = 23
en = 25
temp1 = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

p = GPIO.PWM(en,1000)

p.start(25)

# set speed
p.ChangeDutyCycle(100)

def open_door():
    print("opening door")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    time.sleep(1.17)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

def close_door():
    print("closing door")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    time.sleep(1.1)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

def rotate(value):
    if value > 0:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    elif value < 0:
        value = value * -1
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
    time.sleep(value/10)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

def test():
    while(1):

        x=input()
        
        if x=='r':
            print("run")
            if(temp1==1):
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                print("forward")
                x='z'
            else:
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                print("backward")
                x='z'


        elif x=='s':
            print("stop")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            x='z'

        elif x=='f':
            print("forward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            temp1=1
            x='z'

        elif x=='b':
            print("backward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            temp1=0
            x='z'

        elif x=='l':
            print("low")
            p.ChangeDutyCycle(25)
            x='z'

        elif x=='m':
            print("medium")
            p.ChangeDutyCycle(50)
            x='z'

        elif x=='h':
            print("high")
            p.ChangeDutyCycle(75)
            x='z'
        
        
        elif x=='e':
            GPIO.cleanup()
            break
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
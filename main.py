import time
import threading
import json

import library.ultrasonic as Sonic
import library.motor as motor
import settings

import RPi.GPIO as GPIO          
import paho.mqtt.client as mqtt

broker_address=settings.BROKER_URL
client = mqtt.Client("Trashcan_" + str(settings.TASHCAN_ID))
client.connect(broker_address) 
client.publish("house/main-light","OFF")

inner_sensor = Sonic.Sonic(26, 19)

def automatic_door():
    door_sensor = Sonic.Sonic(16, 20)
    while 1:
        time.sleep(0.1)
        if door_sensor.measure_distance() < 10:
            motor.open_door()
            client.publish("trashcan/{}/door".format(settings.TASHCAN_ID), json.dumps({"id":settings.TASHCAN_ID}))
            time.sleep(5)
            motor.close_door()
            client.publish(
                "trashcan/{}/internal_status".format(settings.TASHCAN_ID),
                json.dumps({"id":settings.TASHCAN_ID, "percentage":inner_sensor.convert_distance_to_percentage(inner_sensor.measure_distance())})
                )
            time.sleep(1)

def percentage_reporter():
    while True:
        time.sleep(10 * 60)

        client.publish(
            "trashcan/{}/internal_status".format(settings.TASHCAN_ID),
            json.dumps({"id":settings.TASHCAN_ID, "percentage":inner_sensor.convert_distance_to_percentage(inner_sensor.measure_distance())})
            )

try:
    threading.Thread(target=percentage_reporter, args=[]).start()
    threading.Thread(target=automatic_door, args=[]).start()
    threading.Thread(target=client.loop_forever(), args=[]).start()
    # door_sensor = Sonic.Sonic(16, 20)
    while 1:
        # motor.rotate(int(input()))
        # motor.open_door()
        # time.sleep(1)
        # motor.close_door()
        # time.sleep(1)
        my_num = inner_sensor.convert_distance_to_percentage(inner_sensor.measure_distance())
        print(my_num)
        time.sleep(1)
        

except KeyboardInterrupt:
    print("exiting safely")
    GPIO.cleanup()
import RPi.GPIO as GPIO
import time

class Ultrasonic_Avoidance:

    def __init__(self, trig, echo):
        GPIO.setmode(GPIO.BCM)
        self.TRIG = trig
        self.ECHO = echo

    def distance(self):

        print "Distance Measurement In Progress"

        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)

        GPIO.output(self.TRIG, False)
        print "Waiting For Sensor To Settle"
        #time.sleep(2)

        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(self.ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        return distance

if __name__ == '__main__':

    sensor = Ultrasonic_Avoidance(20, 16)
    print sensor.distance()

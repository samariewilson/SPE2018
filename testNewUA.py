import time
import RPi.GPIO as GPIO

class Ultrasonic_Avoidance:
    timeout = 0.05

    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        GPIO.setmode(GPIO.BCM)

    def distance(self):
        pulse_end = 0
        pulse_start = 0

        print(self.trig, self.echo)

        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

        GPIO.output(self.trig, GPIO.LOW)

        print("Waiting for sensor to settle")
        time.sleep(2)
        print("Calculating distance")

        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig, GPIO.LOW)

        timeout_start = time.time()
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
          # Computes distance
            if pulse_start != 0 and pulse_end != 0:
                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration * 100 * 343.0 / 2
                distance = int(distance)
          # print 'start = %s'%pulse_start,
          # print 'end = %s'%pulse_end
                if distance >= 0:
                    return distance
                else:
                    return -1
            else:
              # print 'start = %s'%pulse_start,
              # print 'end = %s'%pulse_end
                return -1


if __name__ == '__main__':
    # trig = 20
    # echo = 16
    def make_Ultrasonic_Avoidance(trig, echo):
        sensor = Ultrasonic_Avoidance(trig, echo)
        return sensor
    threshold = 10
    sensor = make_Ultrasonic_Avoidance(20,16)
    distance = sensor.distance()
    print(distance)

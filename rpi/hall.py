import RPi.GPIO as GPIO
import signal
import sys
import time

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def sensor_callback(channel):
    print("Field detected!")
    global callback_entered
    global last_time
    global current_time
    if callback_entered:
        current_time = time.time()*1000
        duration = current_time - last_time
        print('Duration: {}ms'.format(duration))
        last_time = current_time
    else:
        last_time = time.time()*1000
        callback_entered = True

HALLPIN = 23

callback_entered = False

last_time = 0
current_time = 0

if __name__ == '__main__':
    print("main started")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(HALLPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(HALLPIN, GPIO.RISING, 
            callback=sensor_callback)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

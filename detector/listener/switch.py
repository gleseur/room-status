u"""
Handles the lights on/off
"""
import RPi.GPIO as GPIO
import signals

GPIO_PIN = 17
GPIO.setup(GPIO_PIN, GPIO.OUT)

def switch_off(sender):
    GPIO.output(GPIO_PIN, GPIO.HIGH)

def switch_on(sender):
    GPIO.output(GPIO_PIN, GPIO.LOW)

signals.setup.connect(switch_off)
signals.motion.connect(switch_on)
signals.idle.connect(switch_off)

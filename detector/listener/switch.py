u"""
Handles the lights on/off
"""
import functools

import RPi.GPIO as GPIO
import signals


SUBSCRIBED_LISTENERS = {
}

def switch_off(sender):
    print "============= Yo off"
    GPIO.output(SUBSCRIBED_LISTENERS[sender.name].gpio_nb, GPIO.HIGH)

def switch_on(sender):
    print "============= Yo on"
    GPIO.output(SUBSCRIBED_LISTENERS[sender.name].gpio_nb, GPIO.LOW)

class Light(object):

    def __init__(self, gpio_nb, name, paired_detector):
        self.name = name
        self.gpio_nb = gpio_nb
        self._paired_detector = paired_detector
        GPIO.setup(gpio_nb, GPIO.OUT)
        # Subscribing to signals
        self.subscribe_signals()
        SUBSCRIBED_LISTENERS[name] = self

    def subscribe_signals(self):
        signals.setup.connect(switch_off, sender=self._paired_detector)
        signals.busy.connect(switch_on, sender=self._paired_detector)
        signals.room_freed.connect(switch_off, sender=self._paired_detector)

u"""
This module contain a class that records the state of the PIR
detector
"""
from __future__ import unicode_literals

import RPi.GPIO as GPIO

import signals


class PirDetector(object):

    TIME_TO_SLEEP = 0.01

    def __init__(self, gpio_nb, name):
        # state 1 means motion is detected (and signal is sent)
        self.current_state = 0
        self.previous_state = 0
        # gpio_nb is the gpio number associated with the detector
        self.gpio_nb = gpio_nb
        self.name = name

    def setup(self):
        GPIO.setup(self.gpio_nb, GPIO.IN)
        while GPIO.input(self.gpio_nb) == 1:
            time.sleep(0.01)
        signals.setup.send(self)

    def detect_motion(self):
        self.current_state = GPIO.input(self.gpio_nb)
        if self._has_detected_new_motion():
            signals.motion.send(self)
            self.previous_state = 1
        if self._has_returned_to_idle():
            signals.idle.send(self)
            self.previous_state = 0

    def _has_detected_new_motion(self):
        return self.current_state == 1 and self.previous_state == 0

    def _has_returned_to_idle(self):
        return self.current_state == 0 and self.previous_state == 1

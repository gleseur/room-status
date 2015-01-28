u"""
This module contain a class that records the state of the PIR
detector
"""
from __future__ import unicode_literals

import RPi.GPIO as GPIO

import signals


class PirDetector(object):

    GPIO_PIR = 7
    TIME_TO_SLEEP = 0.01

    def __init__(self):
        # state 1 means motion is detected (and signal is sent)
        self.current_state = 0
        self.previous_state = 0

    def setup(self):
        GPIO.setup(self.GPIO_PIR, GPIO.IN)
        while GPIO.input(self.GPIO_PIR) == 1:
            time.sleep(0.01)
        signals.setup.send(self)

    def detect_motion(self):
        self.current_state = GPIO.input(self.GPIO_PIR)
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

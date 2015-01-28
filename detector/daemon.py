u"""
This is the daemon that must be launched in order to detect motion
and launch signals.
"""
from __future__ import unicode_literals

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from detection import PirDetector

# Importing motion listeners
import listener.raspberry_out
import listener.switch

TIME_TO_SLEEP = 0.01


def run_daemon():
    print "Starting Detector daemon"
    detector = PirDetector()
    detector.setup()
    while True:
        detector.detect_motion()
        time.sleep(TIME_TO_SLEEP)

if __name__ == "__main__":
    try:
        run_daemon()
    except KeyboardInterrupt:
        print "Cleaning up GPIO"
        GPIO.cleanup()
        print "Quitting ..."
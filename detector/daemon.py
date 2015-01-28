u"""
This is the daemon that must be launched in order to detect motion
and launch signals.
"""
from __future__ import unicode_literals

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from detection import PirDetector
import settings

# Importing motion listeners
from listener.switch import Light
import listener.raspberry_out

TIME_TO_SLEEP = 0.01

def initialize_detection_pairs():
    detectors = []
    for pair, values in settings.DETECTION_PAIRS.iteritems():
        print "Initializing pair {}".format(pair)
        detector = PirDetector(values["pir"], pair)
        detector.setup()
        detectors.append(detector)
        Light(values["light"], pair, detector)
    return detectors

def run_daemon():
    detectors = initialize_detection_pairs()
    while True:
        for detector in detectors:
            detector.detect_motion()
        time.sleep(TIME_TO_SLEEP)

if __name__ == "__main__":
    try:
        run_daemon()
    except KeyboardInterrupt:
        print "Cleaning up GPIO"
        GPIO.cleanup()
        print "Quitting ..."

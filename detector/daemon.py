u"""
This is the daemon that must be launched in order to detect motion
and launch signals.
"""
from __future__ import unicode_literals

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from detection import PirDetector
from busy_processor import RoomBusyStatus
import settings

# Importing motion listeners
from listener.switch import Light
import listener.raspberry_out

TIME_TO_SLEEP = 0.01

def initialize_detection_pairs():
    detectors = []
    room_statuses = []
    for pair_name, values in settings.DETECTION_PAIRS.iteritems():
        print "Initializing pair {}".format(pair_name)
        detector = PirDetector(values["pir"], pair_name)
        detector.setup()
        detectors.append(detector)
        room_statuses.append(RoomBusyStatus(pair_name, values["free_time"], detector))
        Light(values["light"], pair_name, detector)
    return detectors, room_statuses

def run_daemon():
    detectors, room_statuses = initialize_detection_pairs()
    while True:
        for detector in detectors:
            detector.detect_motion()
        for room_status in room_statuses:
            room_status.check_idle()
        time.sleep(TIME_TO_SLEEP)

if __name__ == "__main__":
    try:
        run_daemon()
    except KeyboardInterrupt:
        print "Cleaning up GPIO"
        GPIO.cleanup()
        print "Quitting ..."
    except Exception as e:
        GPIO.cleanup()
        raise

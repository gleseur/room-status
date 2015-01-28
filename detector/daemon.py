u"""
This is the daemon that must be launched in order to detect motion
and launch signals.
"""
from __future__ import unicode_literals
from detection import PirDetector

TIME_TO_SLEEP = 1

def run_daemon():
    print "Starting Detector daemon"
    detector = PirDetector()
    detector.setup()
    while True:
        detector.detect_motion()
        time.sleep(0.01)

if __name__ == "__main__":
    try:
        run_daemon()
    except KeyboardInterrupt:
        print "Cleaning up GPIO"
        GPIO.cleanup()
        print "Quitting ..."

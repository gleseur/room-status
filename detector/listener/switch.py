u"""
Handles the lights on/off
"""
import RPi.GPIO as GPIO
import signals


class Light(object):

    def __init__(self, gpio_nb, name, paired_detector):
        self.name = name
        self.gpio_nb = gpio_nb
        self._paired_detector = paired_detector
        GPIO.setup(gpio_nb, GPIO.OUT)
        # Subscribing to signals
        self.subscribe_signals()

    def subscribe_signals(self):
        signals.setup.connect(self.switch_off, sender=self._paired_detector)
        signals.busy.connect(self.switch_on, sender=self._paired_detector)
        signals.room_freed.connect(self.switch_off, sender=self._paired_detector)

    def switch_off(sender):
        GPIO.output(self.gpio_nb, GPIO.HIGH)

    def switch_on(sender):
        GPIO.output(self.gpio_nb, GPIO.LOW)

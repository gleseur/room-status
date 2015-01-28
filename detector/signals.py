u"""
Lists the signals that can be registered throughout the app
"""
from __future__ import unicode_literals
from blinker import signal


__all__ = ["setup", "motion", "idle"]

setup = signal("setup")
motion = signal("motion")
idle = signal("idle")

u"""
Lists the signals that can be registered throughout the app
"""
from __future__ import unicode_literals
from blinker import signals


__all__ = ["setup", "motion", "idle"]

setup = signals("setup")
motion = signals("motion")
idle = signals("idle")

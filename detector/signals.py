u"""
Lists the signals that can be registered throughout the app
"""
from __future__ import unicode_literals
from blinker import signal


__all__ = ["setup", "motion", "idle", "busy", "room_freed"]

# Low level signals from PIR
setup = signal("setup")
motion = signal("motion")
idle = signal("idle")
# App level signals
busy = signal("busy")
room_freed = signal("room_freed")

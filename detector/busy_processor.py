u"""
This module computes if the room has been busy for a while or not
"""
import datetime

import settings
import signals


class RoomBusyStatus(object):

    def __init__(self, name, free_time, paired_detector):
        self.name = name
        self.paired_detector = paired_detector
        self.free_time = free_time
        # Internals
        self.is_busy = False
        self.last_motion_at = None
        self._connect_signals()

    def _connect_signals(self):
        signals.motion.connect(self.get_busy, sender=self.paired_detector)

    def get_busy(self, sender):
        if not self.is_busy:
            signals.busy.send(self)
        self.is_busy = True
        self.last_motion_at = datetime.datetime.now()

    def get_idle(self):
        self.is_busy = False
        signals.room_freed.send(self)

    def check_idle(self):
        if self.is_busy and \
                (datetime.datetime.now() - self.last_motion_at).total_seconds() > self.free_time:
            self.get_idle()

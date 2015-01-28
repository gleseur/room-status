u"""
This module computes if the room has been busy for a while or not
"""
import datetime

import settings
import signals



class RoomBusyStatus(object):

    def __init__(self, name, free_time, lock_time, paired_detector):
        self.name = name
        self.paired_detector = paired_detector
        self.free_time = free_time
        self.lock_time = lock_time
        # Internals
        self.is_busy = False
        self.last_motion_at = None
        self.got_idle_at = datetime.datetime.now()
        self._connect_signals()

    def _connect_signals(self):
        signals.motion.connect(self.get_busy, sender=self.paired_detector)

    def get_busy(self, sender):
        if self.seconds_to_now(self.got_idle_at) > self.lock_time:
            return
        if not self.is_busy:
            signals.busy.send(self)
        self.is_busy = True
        self.last_motion_at = datetime.datetime.now()

    def get_idle(self):
        self.is_busy = False
        self.got_idle_at = datetime.datetime.now()
        signals.room_freed.send(self)

    def check_idle(self):
        if self.is_busy and self.seconds_to_now(self.last_motion_at) > self.free_time:
            self.get_idle()

    def seconds_to_now(self, my_date):
        return (datetime.datetime.now() - my_date).total_seconds()

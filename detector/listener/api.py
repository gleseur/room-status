u"""
This listens to room status update and sends relevant HTTP
calls to the meteor app.
"""
from __future__ import unicode_literals

import requests

import signals
import settings

class ApiListener(object):

    API_BUSY = ""

    def __init__(self, room_id, paired_rbs):
        self.room_id = room_id
        self.paired_rbs = paired_rbs
        self._register_signals()

    def _register_signals(self):
        signals.busy.connect(self.send_busy_to_api, sender=self.paired_rbs)
        signals.room_freed.connect(self.send_freed_to_api, sender=self.paired_rbs)

    def send_to_api(self, status):
        url = settings.METEOR_API_URL + "/{room_id}/{status}".format(room_id=self.room_id, status=status)
        r = requests.get(settings.METEOR_API_URL, params={"pwd": settings.METEOR_PASSWORD})
        print "Response status {}".format(r.status_code)

    def send_busy_to_api(self):
        self.send_to_api("busy")

    def send_freed_to_api(self):
        self.send_to_api("free")

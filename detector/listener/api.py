u"""
This listens to room status update and sends relevant HTTP
calls to the meteor app.
"""
from __future__ import unicode_literals

import requests

import signals
import settings

SUBSCRIBED_LISTENERS = {}

def send_busy_to_api(sender):
    SUBSCRIBED_LISTENERS[sender.name].send_to_api("busy")

def send_freed_to_api(sender):
    SUBSCRIBED_LISTENERS[sender.name].send_to_api("free")


retriable_adapter = requests.adapters.HTTPAdapter(max_retries=5)
session = requests.Session()
session.mount("http://wc-status.meteor.com", retriable_adapter)

class ApiListener(object):

    API_BUSY = ""

    def __init__(self, name, room_id, paired_rbs):
        self.room_id = room_id
        self.name = name
        self.paired_rbs = paired_rbs
        self._register_signals()
        SUBSCRIBED_LISTENERS[name] = self

    def _register_signals(self):
        signals.busy.connect(send_busy_to_api, sender=self.paired_rbs)
        signals.room_freed.connect(send_freed_to_api, sender=self.paired_rbs)

    def send_to_api(self, status):
        url = settings.METEOR_API_URL + "/set_status/{room_id}/{status}".format(room_id=self.room_id, status=status)
        try:
            r = session.get(url, params={"pwd": settings.METEOR_PASSWORD})
        except requests.exceptions.ConnectionError:
            print "Could not reach API"
        else:
            print "Response status {}".format(r.status_code)

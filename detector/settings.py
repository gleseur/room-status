u"""
Here we define the settings for the detection
"""
from __future__ import unicode_literals

import local_settings


DETECTION_PAIRS = {
    "male": {
        "room_id": 1,  # To communicate with Meteor API
        "pir": 7,
        "light": 17,
        "free_time": 20,  # time in seconds after which we deem the room freed
        "lock_time": 1,  # time in seconds before which we deem there can be someone else in the room
    },
    "female": {
        "room_id": 2,  # To communicate with Meteor API
        "pir": 8,
        "light": 23,
        "free_time": 20,  # time in seconds after which we deem the room freed
        "lock_time": 1,  # time in seconds before which we deem there can be someone else in the room
    }
}

METEOR_API_URL = "http://wc-status.meteor.com"
METEOR_PASSWORD = local_settings.METEOR_PASSWORD

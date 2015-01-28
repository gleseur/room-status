u"""
Here we define the settings for the detection
"""
from __future__ import unicode_literals

DETECTION_PAIRS = {
    "male": {
        "id": 1,  # To communicate with Meteor API
        "pir": 7,
        "light": 17,
        "free_time": 5,  # time in seconds after which we deem the room freed
        "lock_time": 2,  # time in seconds before which we deem there can be someone else in the room
    }
}
